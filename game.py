from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Qt, QTimer, QThread, Signal
from PySide2.QtGui import QMovie, QFont, QFontDatabase

from game_ui import Ui_MainWindow  # Import the generated UI file
from volumeMixer import set_volume

import os, time
import sys
import socket
import json
from dotenv import load_dotenv
from client import *


def get_player_list(server_data, server_name):
    for server in server_data:
        print(f"Get Player List: {server['server_name']}, user server_name: {server_name}")
        if server['server_name'] == server_name:
            return server['players']



def restart_program():
    os.system('cls' if os.name == 'nt' else 'clear')
    game = sys.executable
    os.execl(game, game, *sys.argv)


def get_score_board(player_list):
    score_board = [(player['name'], player['rolls']) for player in player_list]
    return sorted(score_board, key=lambda x: x[1][0], reverse=True)


def ExitGame():
    QApplication.quit()
    sys.exit(app.exec_())


class UpdateThread(QThread):
    update_received = Signal(object)

    def __init__(self, update_port):
        super().__init__()
        self.update_port = update_port
        self.stop_update_thread = False

    def run(self):
        update_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        update_socket.bind((socket.gethostbyname(socket.gethostname()), self.update_port))
        print(f"Update channel is listening on port {self.update_port}")

        while not self.stop_update_thread:
            try:
                update_socket.settimeout(1)
                data, _ = update_socket.recvfrom(4096)
                data = json.loads(data.decode())
                print('Update received:', data)
                self.update_received.emit(data)
            except socket.timeout:
                continue
        update_socket.close()
        print("Update listening thread stopped.")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # SETTING UP UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.isFullScreen()

        # General
        self.user_name = user_name

        self.font_path = os.path.abspath("assets/font/SAOUI-Regular.otf")

        QFontDatabase.addApplicationFont(self.font_path)
        self.custom_font = QFont()
        self.custom_font.setFamily("sao-ui")
        app.setFont(self.custom_font)

        print(f'GAME PLAYING AS: {self.user_name}')
        gif_path = [r'assets\animation\dice1.gif', r'assets\animation\dice2.gif', r'assets\animation\dice3.gif']
        random_gif = random.choice(gif_path)
        absolute_path = os.path.abspath(random_gif)
        self.movie_url = absolute_path.replace(r'\Game', '')
        self.movie_stay_url = os.path.abspath(r'assets\animation\stay.gif').replace(r'\Game', '')

        print(self.movie_url)
        print(self.movie_stay_url)
        print(self.font_path)

        self.isHowtoPlayPage = False

        # LOCAL GAME DATA
        self.bot_index = 0
        self.local_players_data = []
        self.remaining_time_L = 0
        self.player_isTurn = False
        self.isTiming = False
        self.inGameSetting = False
        self.ingamerate = 1000
        self.ingametime = 60 * 1000
        self.highest_game_value = 26
        self.notExit = True

        self.local_scoreBoard = []
        self.player_data_local = {
            'name': self.user_name,
            'rolls': [],
            'current_bet': '',
        }

        self.Local_Data = [
            {
                'name': 'Bot 2',
                'turn': '2',
                'rolls': [],
                'current_bet': '',
            },
            {
                'name': 'Bot 3',
                'turn': '3',
                'rolls': [],
                'current_bet': '',
            },
            {
                'name': 'Bot 4',
                'turn': '4',
                'rolls': [],
                'current_bet': '',
            }
        ]

        # LOCAL GAME INTERACTIVE
        self.ui.roll_button.clicked.connect(self.check_valid_turn)
        self.roll_button_clicked = False
        self.ui.roll_button.clicked.connect(self.set_roll_button_clicked)

        self.timerL = QTimer()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_ingame_timer)

        # 0 for AI, 1 for Multiplayer
        self.total_dice_amount = 5
        self.current_player = 0
        self.local_total_dice_roll = []

        self.movie = None
        self.Servers_List = []

        # ONLINE
        self.isJoinedOnline = False
        self.online_mode = ['Poor', 'Middle Class', 'Rich', 'Mafia Boss']
        try:
            self.DisplayOnlineServers()
            print('GAME: Connected to online servers.')
        except ConnectionResetError:
            print('GAME: Unable To Display Online Servers, Please Connect To the Internet or Wait for Server To be Hosted!')

        # Initialised
        self.ui.host_server_name.setText(f"{self.player_data_local['name']}'s Server")
        self.ui.InGameSettingWidget.hide()
        self.bots = 0
        self.ui.server_warning.hide()
        self.ui.Content.setCurrentIndex(0)
        self.ui.LobbyPlayersTab.clear()
        self.ui.split_bet_button.hide()
        self.ui.host_player_count.setValue(4)
        self.update_thread = UpdateThread(update_port=update_port)
        self.update_thread.update_received.connect(self.UpdateNavigation)
        self.update_thread.start()
        self.ui.logged_in_name.setText(self.user_name)
        self.ui.logged_in_ip.setText(client_name)

        # Set Sound Volume
        self.general_volume = self.ui.volume_slider_general.value()
        #self.sfx_volume = self.ui.volume_slider_sfx.value()
        #self.music_volume = self.ui.volume_slider_music.value()
        # Button
        self.ui.online_button.clicked.connect(self.PageSwitchOnline)
        self.ui.local_button.clicked.connect(self.PageSwitchLocal)
        self.ui.hostgame_backbutton.clicked.connect(lambda: self.PageSwitchHostGame(1))
        self.ui.server_back_button.clicked.connect(self.ResetPages)
        self.ui.hostgame_backbutton.clicked.connect(self.ResetPages)
        self.ui.server_back_button.clicked.connect(lambda: self.ui.Content.setCurrentIndex(0))
        self.ui.settings_button.clicked.connect(lambda: self.ui.Content.setCurrentIndex(2))
        self.ui.setting_back_button.clicked.connect(lambda: self.ui.Content.setCurrentIndex(0))
        self.ui.quit_button.clicked.connect(ExitGame)
        self.ui.create_server_button.clicked.connect(self.CreateServerSwitch)

        #Server List
        self.ui.refresh_sever.clicked.connect(self.DisplayOnlineServers)
        self.ui.server_list.itemClicked.connect(self.OnClickServersItem)

        # In LOCAL GAME BUTTOn
        self.ui.setting_button.clicked.connect(self.ui.InGameSettingWidget.show)
        self.ui.game_return.clicked.connect(self.ui.InGameSettingWidget.hide)
        self.ui.game_leave.clicked.connect(restart_program)
        #self.ui.game_leave.clicked.connect(self.Reset_Game)
        self.ui.game_quit.clicked.connect(ExitGame)
        self.ui.volume_slider_general.sliderMoved.connect(self.VolumeSliderMove)
        self.ui.about_button.clicked.connect(lambda: self.ui.Content.setCurrentIndex(3))
        self.ui.about_back_button.clicked.connect(self.SwitchSettingBackButton)
        self.ui.local_create_game.clicked.connect(self.SettingUpLocal)
        self.ui.local_howto_play.clicked.connect(self.SwitchPageHowToPlay)
        self.ui.host_creategame.clicked.connect(self.StartServer)
        self.ui.LobbyLeaveGame.clicked.connect(self.LeaveServer)
        self.ui.local_playercount.valueChanged.connect(self.local_update_ai)

        #ONLINE MULTIPLAYER
        self.ui.LobbyStartGameButton.clicked.connect(self.HostStartGameServer)
        self.CurrentServerName = ""
        self.OnlineServerPlayerOrder = []
        self.isOnlineHost = False
        self.OnlineCurrentRound = 0
        self.OnlineMovieDice = QMovie(self.movie_url)
        self.OnlineMovieDice.setScaledSize(self.ui.OnlineDiceAnimation.size())

        self.OnlineMovieStay = QMovie(self.movie_stay_url)
        self.OnlineMovieStay.setScaledSize(self.ui.OnlineStayAnimation.size())

        self.OnlineGameCurrentIndex = 0
        self.OnlineGameCurrentPlayer = ''
        self.OnlineGameNextPlayer = ''
        self.OnlineGameSelfDice = 0

        self.ui.OnlineDiceRollNumber.setText("")

        self.ui.OnlineRollButton.clicked.connect(self.OnlineRollDice)
        self.ui.OnlineStayButton.clicked.connect(self.OnlineStayDice)

        self.OnlineFirstAndLastTurn = []
        self.OnlineGameEndRoundScoreBoard = []
        self.ui.OnlineGameTableStacked.setCurrentIndex(0)
        self.ui.OnlineGameScoreBoard.clear()
        self.ui.OnlineGameEndText.hide()
        self.ui.OnlineLeaveGameButton.hide()
        self.ui.OnlineLeaveGameButton.clicked.connect(self.LeaveEndGame)

    def LeaveEndGame(self):
        try:
            RequestLeaveServer(f'server/{self.CurrentServerName}')
            self.LeaveServer()
        except Exception:
            pass

        self.ExitGame()



    def ResetOnlineGame(self):
        self.CurrentServerName = ""
        self.OnlineServerPlayerOrder = []
        self.isOnlineHost = False
        self.OnlineCurrentRound = 0

        self.OnlineGameCurrentIndex = 0
        self.OnlineGameCurrentPlayer = ''
        self.OnlineGameNextPlayer = ''
        self.OnlineGameSelfDice = 0
        self.ui.OnlineCurrentRound.setText('Round: 0/3')

        self.ui.OnlineDiceRollNumber.setText("")

        self.OnlineFirstAndLastTurn = []
        self.OnlineGameEndRoundScoreBoard = []
        self.ui.OnlineGameTableStacked.setCurrentIndex(0)
        self.ui.OnlineGameScoreBoard.clear()
        self.ui.OnlineGameEndText.hide()
        self.ui.OnlineLeaveGameButton.hide()
        self.ui.TurnNavigator.show()

        #Extras



    def UpdateNavigation(self, data):
        #list of command /update_join /update_leave
        #print('PRINT DATA:', data)
        if data[0] == 'update_join':
            self.UpdatePlayerServerLobby(playerList=data[1])
        elif data[0] == 'update_leave':
            self.RemovePlayerFromLobby(name=data[1])
        elif data[0] == 'update_host_leave':
            self.HostLeaveServer()
        elif data[0] == 'update_game_start':
            self.PlayersStartGameServer()
        elif data[0] == 'update_game_roll_dice':
            #change dice on everyone's screen and update
            self.PlayerUpdateDice(data[1])
        elif data[0] == 'update_game_stay_dice':
            #change dice on everyone's screen and update
            self.PlayerStayDice(data[1], data[2])
        elif data[0] == 'request_highest_player_rolls':
            self.PlayerUpdateScoreBoard(data[1])



    def PlayerUpdateScoreBoard(self, roll_list):
        sorted_data = sorted(roll_list, key=lambda x: int(x[1]), reverse=True)
        self.ui.OnlineGameScoreBoard.clear()
        for players in sorted_data:
            if self.user_name == players[0]:
                self.ui.OnlineGameScoreBoard.addItem(f'{players[0]} ~ {players[1]} (You)')
            else:
                self.ui.OnlineGameScoreBoard.addItem(f'{players[0]} ~ {players[1]}')
        if self.ui.OnlineGameScoreBoard.item(0) is not None:
            self.ui.OnlineGameEndText.setText(f'Congratulations {self.ui.OnlineGameScoreBoard.item(0).text()} You are the Winner!!')


    def OnlinePlayDiceAnimation(self):
        self.ui.OnlineDiceAnimation.setMovie(self.OnlineMovieDice)
        self.OnlineMovieDice.start()

    def PlayerUpdateDice(self, dice):
        self.ui.OnlineDiceRollNumber.setText(str(dice))
        self.OnlinePlayDiceAnimation()

        #Wait 5 seconds
        QTimer.singleShot(4000, self.OnlineChangeTurnByClick)


    def OnlinePlayStayAnimation(self):
        self.ui.OnlineStayAnimation.setMovie(self.OnlineMovieStay)
        self.OnlineMovieStay.start()

    def PlayerStayDice(self, dice, name):
        self.ui.OnlineDiceRollNumber.setText(f'{name} Chooses to Stay with: {dice}')
        self.OnlinePlayStayAnimation()
        #Wait 5 seconds
        QTimer.singleShot(4000, self.OnlineChangeTurnByClick)






    def HostStartGameServer(self):
        #Checks if there is  minimum 2 players
        if self.ui.LobbyPlayersTab.count() < 2:
            #Cant start game
            print(f'ONLINE SERVER: UNABLE TO START GAME (NOT ENOUGH PLAYERS) MIN 2 PLAYERS, CURRENTLY {self.ui.LobbyPlayersTab.count()}/2')
        else:
            SendInstructionToServer(server_name=self.ui.LobbyServerName.text(), instruction='update_game_start', data=self.ui.LobbyServerName.text())


    def PlayersStartGameServer(self):
        self.CurrentServerName = self.ui.LobbyServerName.text()
        playerList = get_player_list(GetAvailableServers(), self.CurrentServerName)
        order_list = []
        for players in playerList:
            order_list.append(players['name'])
        order_list.append('Round End')

        self.OnlineServerPlayerOrder = order_list
        self.OnlineFirstAndLastTurn = [self.OnlineServerPlayerOrder[0], self.OnlineServerPlayerOrder[-1], 'Round End']

        #print(f'ONLINE GAME PLAYER TURN ORDER: {self.OnlineServerPlayerOrder}')
        self.ResetLobby()
        self.ui.Content.setCurrentIndex(5)
        #print("ONLINE GAME SERVER STARTED! ENJOY!")

        #Starts Online Game
        self.OnlineGameStart()


    def OnlineRollDice(self):
        roll_list, dice_amount = self.generate_dice()
        self.OnlineGameSelfDice = dice_amount
        SendInstructionToServer(server_name=self.CurrentServerName, instruction='update_game_roll_dice', data=f'{dice_amount}/{self.user_name}/{self.CurrentServerName}')
        self.ui.OnlineWidget.hide()

    def OnlineStayDice(self):
        SendInstructionToServer(server_name=self.CurrentServerName, instruction='update_game_stay_dice', data=f'{self.OnlineGameSelfDice}/{self.user_name}/{self.CurrentServerName}')
        self.ui.OnlineWidget.hide()



    def OnlineGameStart(self):
        self.ui.OnlineWidget.hide()
        self.OnlineCurrentRound = 0
        Host = self.OnlineServerPlayerOrder[0]

        self.ui.LobbyCurrentTurn.setText(Host)
        self.ui.OnlineCurrentPlayerNameLabel.setText(self.user_name)
        self.ui.LobbyNextTurn.setText(self.OnlineServerPlayerOrder[1])

        if user_name == Host:
            #First Turn Player Start
            self.isOnlineHost = True
            self.ui.OnlinePlayerIndicator.setText(f'Your Turn')

            self.ui.OnlineWidget.show()
            if self.OnlineCurrentRound == 0:
                # unable to press hold.
                self.ui.OnlineStayButton.hide()
            else:
                self.ui.OnlineStayButton.show()





        elif user_name != Host and user_name in self.OnlineServerPlayerOrder:
            self.isOnlineHost = False
            self.ui.OnlinePlayerIndicator.setText(f'Current Watching {Host}')

    def get_next_index(self, index_list, fixed=True):
        next_index = (self.OnlineGameCurrentIndex + 1) % len(index_list)
        if fixed: self.OnlineGameCurrentIndex = next_index
        return index_list[next_index]


    def OnlineChangeTurnResume(self):
        self.ui.OnlineGameScoreBoard.clear()
        self.ui.OnlineGameTableStacked.setCurrentIndex(0)
        self.OnlineGameNextPlayer = self.get_next_index(self.OnlineServerPlayerOrder)
        self.OnlineChangeTurnByClick(isFixed=False)


    def OnlineChangeTurnByClick(self, isFixed=True):
        #print('Change turn into ', self.OnlineServerPlayerOrder)
        #update next turn
        self.OnlineMovieDice.stop()
        self.OnlineMovieStay.stop()
        self.ui.OnlineDiceAnimation.clear()
        self.ui.OnlineStayAnimation.clear()
        self.ui.OnlineDiceRollNumber.setText("")

        if isFixed:
            self.OnlineGameCurrentPlayer = self.get_next_index(self.OnlineServerPlayerOrder)
        else:
            self.OnlineGameCurrentPlayer = self.OnlineServerPlayerOrder[0]
        self.ui.LobbyCurrentTurn.setText(self.OnlineGameCurrentPlayer)

        self.OnlineGameNextPlayer = self.get_next_index(self.OnlineServerPlayerOrder, fixed=False)
        self.ui.LobbyNextTurn.setText(self.OnlineGameNextPlayer)






        #print(f'GAME: Current Player Turn: {self.OnlineGameCurrentPlayer}, You are: {self.user_name}')
        if self.OnlineGameCurrentPlayer == self.user_name and self.OnlineCurrentRound < 3:
            #If next turn is you
            self.ui.OnlinePlayerIndicator.setText('Your Turn')
            self.ui.OnlineWidget.show()
            if self.OnlineCurrentRound == 0:
                self.ui.OnlineStayButton.hide()
            else:
                self.ui.OnlineStayButton.show()

        elif self.OnlineGameCurrentPlayer != self.user_name and self.user_name in self.OnlineServerPlayerOrder and self.OnlineCurrentRound < 3:
            #If next turn is not you
            self.ui.OnlinePlayerIndicator.setText(f'Currently Watching: {self.OnlineGameCurrentPlayer}')
            self.ui.OnlineWidget.hide()


        print(f'ROUND: {self.OnlineCurrentRound}, CURRENT PLAYER {self.OnlineGameCurrentPlayer}, NEXT PLAYER {self.OnlineGameNextPlayer}')

        if self.OnlineCurrentRound >= 3:
            # End Game with total score
            self.ui.OnlineCurrentRound.setText('Game End')
            self.ui.OnlineWidget.hide()
            self.ui.TurnNavigator.hide()
            self.ui.OnlineGameTableStacked.setCurrentIndex(1)

            SendInstructionToServer(server_name=self.CurrentServerName, instruction='request_highest_player_rolls')
            self.ui.OnlineGameEndText.show()
            self.ui.OnlineLeaveGameButton.show()


        # If reached the end of index and next player = last player round += 1, round finishs move on to next one
        if self.OnlineGameCurrentPlayer == self.OnlineFirstAndLastTurn[-1] and self.OnlineGameNextPlayer == self.OnlineFirstAndLastTurn[0]:
            if self.OnlineCurrentRound < 3:
                self.OnlineCurrentRound += 1
                self.ui.OnlineCurrentRound.setText(f'Round: {self.OnlineCurrentRound}/3')
                self.ui.OnlineGameTableStacked.setCurrentIndex(1)
                self.ui.OnlineWidget.hide()

                # Get instruction and return name with the highest roll dice per round
                SendInstructionToServer(server_name=self.CurrentServerName,
                                        instruction='request_highest_player_rolls')
                QTimer.singleShot(7000, self.OnlineChangeTurnResume)


    def HostLeaveServer(self):
        self.ResetOnlineGame()
        self.ui.Content.setCurrentIndex(1)
        self.ui.PlayPageStackedWidget.setCurrentIndex(0)
        self.ResetLobby()
        self.DisplayOnlineServers()
        self.ui.server_back_button.show()

    def RemovePlayerFromLobby(self, name):

        items = self.ui.LobbyPlayersTab.findItems(name, Qt.MatchExactly)
        for item in items:
            #print(f'LOBBY PLAYERS {name} HAS LEFT!')
            self.ui.LobbyPlayersTab.takeItem(self.ui.LobbyPlayersTab.row(item))
            # Only remove the first match if we want to stop after one removal
            # break
            break




    def UpdatePlayerServerLobby(self, playerList):
        #print('UPDATE SERVER LOBBY')
        self.ui.LobbyPlayersTab.clear()
        for players in playerList:
            #print('LOBBY ADDING PLAYERS:', players)
            self.ui.LobbyPlayersTab.addItem(players)
        if self.ui.LobbyPlayersTab.item(0) is not None:
            self.ui.LobbyHostName.setText(self.ui.LobbyPlayersTab.item(0).text())

    def CreateServerSwitch(self):
        self.ui.server_warning.hide()
        self.PageSwitchHostGame(0)


    def SwitchSettingBackButton(self):
        if self.isHowtoPlayPage is True:
            self.ui.Content.setCurrentIndex(1)
            self.ui.PlayPageStackedWidget.setCurrentIndex(2)
            self.isHowtoPlayPage = False
        else:
            self.ui.Content.setCurrentIndex(0)

    def VolumeSliderMove(self):
        value = int(self.ui.volume_slider_general.value()) / 100
        #print(value)
        set_volume(value)

    def SwitchPageHowToPlay(self):
        self.ui.Content.setCurrentIndex(3)
        self.isHowtoPlayPage = True


    def OnClickServersItem(self, item):
        self.isJoinedOnline = True
        server = str(item.text())
        request = RequestJoinServer(target=server)
        #print(request)
        try:
            if request[0] is True:
                self.ResetLobby()
                instance = request[1]
                self.ui.PlayPageStackedWidget.setCurrentIndex(3)
                self.ui.server_back_button.hide()
                self.ui.LobbyStartGameButton.hide()
                self.ui.LobbyServerName.setText(instance['server_name'])
                self.ui.LobbyMaxPlayer.setText(str(instance['server_size']))



                #print(f'request: {request}')
                #for players in request[1]['players']:
                #    print(players)
                #    self.ui.LobbyPlayersTab.addItem(players['name'])
                #print(request[1])

            else:
                print('Server is Full')
        except TypeError:
            print('Server is Full')
            pass




    def DisplayOnlineServers(self):
        try:
            servers_dict = GetAvailableServers()
            self.ui.server_list.clear( )
            for servers in servers_dict:
                item = f"{servers['server_name']}: {servers['server_current_player']}/{servers['server_size']}"
                #print(item)
                self.ui.server_list.addItem(item)
        except TypeError:
            self.ui.server_list.clear()

    def ResetLobby(self):
        self.ui.LobbyStartGameButton.show()
        self.ui.LobbyPlayersTab.clear()
        self.ui.LobbyMaxPlayer.clear()
        self.ui.LobbyServerName.clear()


    def LeaveServer(self):
        self.ui.PlayPageStackedWidget.setCurrentIndex(0)
        self.ui.server_back_button.show()
        self.ui.LobbyStartGameButton.show()
        self.ui.LobbyHostName.setText("")

        if self.isJoinedOnline:
            self.isJoinedOnline = False
            if RequestLeaveServer(f'user/{self.user_name}'): #IF Server side is removedz
                item_name = self.user_name

                for index in range(self.ui.LobbyPlayersTab.count()):
                    item = self.ui.LobbyPlayersTab.item(index)
                    if item.text() == item_name:
                        self.ui.LobbyPlayersTab.takeItem(index)
                        break


        elif not self.isJoinedOnline:
            # Function to remove a segment based on server_name
            if RequestLeaveServer(f'server/{self.ui.LobbyServerName.text()}'):
                self.ResetLobby()


    def StartServer(self):
        if self.ui.host_server_name.text() in self.Servers_List:
            self.ui.server_warning.show()
        elif self.ui.host_server_name.text() not in self.Servers_List:
            self.ui.server_back_button.hide()

            server_data = self.receive_host_information()
            #UI

            self.ui.PlayPageStackedWidget.setCurrentIndex(3)

            #Get Data
            self.ui.LobbyServerName.setText(server_data[0])
            self.ui.LobbyMaxPlayer.setText(str(server_data[1]))
            self.ui.LobbyPlayersTab.clear()

            #Run server scripts
            if RequestCreateServer(usr_name=self.user_name, server_name=server_data[0], size=server_data[1]):
                self.ui.LobbyPlayersTab.addItem(self.user_name)
            self.ui.LobbyHostName.setText(self.ui.LobbyPlayersTab.item(0).text())



            #print(server_data)



    def receive_host_information(self):
        #print(self.ui.host_server_name.text())
        server_name = str(self.ui.host_server_name.text())
        player_count = int(self.ui.host_player_count.value())
        server_mode = self.ui.host_mode.currentIndex()
        self.ui.host_server_name.setText(f"{self.user_name.capitalize()}'s Server")
        self.ui.host_player_count.setValue(2)
        self.ui.host_mode.setCurrentIndex(0)


        return [server_name, player_count, server_mode]




    def calculate_gif_length(self):
        frame_count = self.movie.frameCount()
        frame_duration = self.movie.nextFrameDelay()  # Returns the duration of the next frame in milliseconds
        gif_length = frame_count * frame_duration
        #print("GIF length:", gif_length, "milliseconds")
        return gif_length


        # During Game While is your turn

    def get_highest_roll(self, roll_list):
        sorted_list = sorted(roll_list, reverse=True)

        highest_amount = None
        for amount in sorted_list:
            if amount <= self.highest_game_value:
                highest_amount = amount
                break

        if highest_amount is not None:
            return highest_amount
        else:
            return 0

    def check_valid_turn(self):
        # if the timing of user is true
        if self.isTiming and self.player_isTurn:
            self.roll_dice()

    def ExitGame(self):
        self.ui.Content.setCurrentIndex(0)
        self.ui.InGameSettingWidget.hide()
        # ReStart Value for Prograrms.

    def local_update_ai(self):
        value = self.ui.local_playercount.value()
        self.ui.local_player_image.setPixmap(f':Local/assets/background/Local/{value}.png')

    def PageSwitchHostGame(self, mode):
        if mode == 0:
            self.ui.server_back_button.hide()
            self.ui.PlayPageStackedWidget.setCurrentIndex(1)
        elif mode == 1:
            self.ui.server_back_button.show()
            self.ui.PlayPageStackedWidget.setCurrentIndex(0)

    def PageSwitchOnline(self):
        self.ui.Content.setCurrentIndex(1)
        self.DisplayOnlineServers()
        self.ui.PlayPageStackedWidget.setCurrentIndex(0)

    def PageSwitchLocal(self):
        self.ui.Content.setCurrentIndex(1)
        self.ui.PlayPageStackedWidget.setCurrentIndex(2)

    def ResetPages(self):
        self.ui.host_server_name.setText(f"{self.user_name}'s Server")
        self.ui.local_playercount.setValue(1)
        self.ui.host_player_count.setValue(1)
        self.ui.host_mode.setCurrentIndex(0)

    def Reset_Game(self, isFirst=False):
        #print('RESETTING GAME')



        # Reset any other necessary variables or UI elements
        self.ui.ingame_timer.setText('60')
        self.ui.bet_amount.setText("$0")

        self.local_total_dice_roll = []

        if not self.local_total_dice_roll:
            self.ui.local_highest_roll.setText("Highest Roll:")

        self.ui.dice_amount.setText("0")
        self.ui.dice_animation_label.clear()


        if not isFirst:
            # Clear any connections to timer timeouts
            self.timer.timeout.disconnect()
            self.timerL.timeout.disconnect()

            # Stop both timers
            self.timer.stop()
            self.timerL.stop()

            self.isTiming = False
            self.roll_button_clicked = True

    def Update_Local_Data(self):
        pass

    def update_ingame_timer(self, start_timer=True):
        if start_timer:
            self.timer.start(1000)  # Start the timer
        else:
            self.timer.stop()  # Stop the timer

        current_text = self.ui.ingame_timer.text()
        current_number = int(current_text)
        current_number -= 1
        self.ui.ingame_timer.setText(str(current_number))
        self.isTiming = True
        if current_number == 0:
            self.timer.stop()
            self.isTiming = False

    def update_dice(self):
        # filtering list
        for n in self.local_total_dice_roll:
            if n >= self.highest_game_value:
                self.local_total_dice_roll.remove(n)

        self.local_total_dice_roll.sort(reverse=True)

        self.ui.local_highest_roll.setText(f'Highest Roll: {str(self.local_total_dice_roll[0])}')
        #print(self.local_total_dice_roll)

    def play_dice_animation(self):
        self.ui.dice_animation_label.setMovie(self.movie)
        self.movie.start()

        delay = 5

        QTimer.singleShot(int(self.calculate_gif_length()) + delay*1000, self.ui.dice_animation_label.clear)




    def generate_player_data(self, amount):
        player_List = [self.player_data_local]

        for player in range(0, amount):
            #print(player)
            new_player_data = {
                'name': f'Player {player+1}',
                'rolls': [],
                'current_bet': ''
            }

            player_List.append(new_player_data)

        #print(player_List)
        return player_List


    def SettingUpLocal(self):
        if self.bots == 0: self.bots = self.ui.local_playercount.value()

        # How many AI Bots
        player = self.bots + 1  # How many player
        self.ui.LocalStackedTable.setCurrentIndex(0)

        self.ui.local_playercount.setValue(1)

        # Reset Game Ensure Refresh Game
        self.Reset_Game(True)
        self.ui.Content.setCurrentIndex(4)
        self.ui.GamePagePanel.setCurrentIndex(0)
        # Setting Game Variable


        #Generating Player Data
        self.local_players_data = self.generate_player_data(self.bots)


        #Setting The Gif for Dice Rolling
        self.movie = QMovie(self.movie_url)
        self.movie.setScaledSize(self.ui.dice_animation_label.size())  # Set the movie size to match the label size

        # game Start
        print('GAME STARTING')
        # await events

        #===================================

        self.player_turn()
        try:
            self.update_dice()
        except Exception as Error:
            print(Error)
            pass
        #===================================


        self.remaining_time_L = 7


        def update_timer_local():
            self.remaining_time_L -= 1
            self.ui.current_player.setText(f'Next Turn Begins in: {str(self.remaining_time_L)}')
            print(f'Next Turn Begins in: {str(self.remaining_time_L)}')
            if self.remaining_time_L <= 0:
                self.timerL.stop()


        self.timerL.timeout.connect(update_timer_local)
        self.timerL.start(1000)
        QTimer.singleShot(7001, self.bots_handling)

        #===================================
        #new Rounds
        #self.local_newRounds()

    def local_newRounds(self):
        def Reset():
            # Reset Game Ui to the first round
            # Front End
            self.ui.LocalStackedTable.setCurrentIndex(0)
            self.ui.current_player.setText('Your Turn')
            self.ui.ingame_timer.setText('60')
            self.ui.local_highest_roll.setText('Highest Roll:')
            self.ui.dice_amount_text.setText('YOU HAVE ROLLED')
            self.ui.dice_amount.setText('0')
            # BackEnd
            self.player_isTurn = False
            self.isTiming = False
            self.timer.stop()
            self.timerL.stop()
            self.SettingUpLocal()

        self.ui.LocalStackedTable.setCurrentIndex(1)
        self.ui.current_player.setText('')
        score_board = get_score_board(self.local_players_data)
        if len(score_board) == 4:
            self.ui.localFirstplace.setText(f'1st: {score_board[0][0]} {score_board[0][1]}')
            self.ui.localSecondplace.setText(f'2nd: {score_board[1][0]} {score_board[1][1]}')
            self.ui.localThirdplace.setText(f'3rd: {score_board[2][0]} {score_board[2][1]}')
            self.ui.localFourthplace.setText(f'4th: {score_board[3][0]} {score_board[3][1]}')
        elif len(score_board) == 3:
            self.ui.localFirstplace.setText(f'1st: {score_board[0][0]} {score_board[0][1]}')
            self.ui.localSecondplace.setText(f'2nd: {score_board[1][0]} {score_board[1][1]}')
            self.ui.localThirdplace.setText(f'3rd: {score_board[2][0]} {score_board[2][1]}')
            self.ui.localFourthplace.setText('')
        elif len(score_board) == 2:
            self.ui.localFirstplace.setText(f'1st: {score_board[0][0]} {score_board[0][1]}')
            self.ui.localSecondplace.setText(f'2nd: {score_board[1][0]} {score_board[1][1]}')
            self.ui.localThirdplace.setText('')
            self.ui.localFourthplace.setText('')
        elif len(score_board) == 1:
            self.ui.localFirstplace.setText(f'1st: {score_board[0][0]} {score_board[0][1]}')
            self.ui.localSecondplace.setText('')
            self.ui.localThirdplace.setText('')
            self.ui.localFourthplace.setText('')



    def set_roll_button_clicked(self):
        self.roll_button_clicked = True

    def player_turn(self):
        print('Current Playing Player 1')
        self.roll_button_clicked = False
        self.timer.stop()
        self.timer.start(self.ingamerate)
        self.isTiming = True
        self.ui.current_player.setText('Your Turn')
        self.player_isTurn = True
        self.timeout_occurred = False  # Flag to track if timeout occurred

        # Define a callback function
        def timeout_handler():
            if not self.roll_button_clicked and self.isTiming:
                pass
            elif not self.roll_button_clicked:
                print("Time's up!")
                self.timeout_occurred = True  # Set flag to indicate timeout
                self.roll_button_clicked = True  # Simulate button click to exit loop

        # Wait for button press or timeout
        while self.isTiming and not self.roll_button_clicked:
            QApplication.processEvents()
            # print(self.isTiming, self.roll_button_clicked)
            timeout_handler()

        # If the timer ran out without button press
        # print(self.roll_button_clicked, self.timeout_occurred)
        if self.timeout_occurred:
            # print('rolling dice')
            self.roll_dice()  # Roll dice automatically
            self.ui.ingame_timer.setText("")

        # Reset flags
        self.roll_button_clicked = False
        self.timeout_occurred = False




    def roll_dice(self):
        dice_list, total_dice = self.generate_dice()
        self.ui.dice_amount_text.setText("YOU HAVE ROLLED")


        self.ui.dice_amount.setText(str(total_dice))
        self.player_isTurn = False  # Set players turn to fasle because move has already gone
        print(f'Total Dice Amount: {total_dice}\nDice Sequences: {dice_list}')
        self.isTiming = False
        self.timer.stop()
        self.play_dice_animation()
        self.player_data_local['rolls'].append(total_dice)
        self.current_player += 1
        self.local_total_dice_roll.append(total_dice)

    def bots_handling(self):
        # Define the index for iterating over self.Local_Data

        # Define a function to handle each iteration of the loop
        self.bot_index = 0

        def handle_iteration():

            def stop_movie():
                #print('stopping movie', self.movie.loopCount())
                self.movie.stop()
            # Check if there are more players to handle
            if self.bot_index < int(self.bots):
                player = self.Local_Data[self.bot_index]
                self.ui.dice_amount.setText("")
                self.ui.dice_amount_text.setText(f"{player['name'].upper()} HAVE ROLLED")
                print(f'Currently Playing: {player["name"]}')
                self.ui.current_player.setText(f'Currently Watching: {player["name"]}')


                # Increment the index for the next iteration
                self.bot_index += 1

                # Set a QTimer to update the text every second
                random_bot_time = random.randint(0, 10)
                #print("Random bot time", random_bot_time)

                self.timer_count = 0
                self.update_timer_text()
                self.timer = QTimer()
                self.timer.timeout.connect(self.update_timer_text)
                self.timer.start(1000)

                def update_dice():
                    dice_list, total_dice = self.generate_dice()
                    self.local_total_dice_roll.append(total_dice)
                    self.update_dice()
                    self.ui.dice_amount.setText(str(total_dice))

                    self.local_players_data[self.bot_index]['rolls'].append(total_dice)
                    print(self.local_players_data)

                # Set a QTimer for 10 seconds to trigger the next iteration


                dice_time_delay = 3 * 1000

                QTimer.singleShot(dice_time_delay, self.play_dice_animation)
                movie_length = self.calculate_gif_length()
                QTimer.singleShot(dice_time_delay + movie_length, update_dice)

                QTimer.singleShot(dice_time_delay + movie_length, stop_movie)

                QTimer.singleShot(10000, handle_iteration)



            else:
                print("All players processed")
                self.local_newRounds()
                #->> go back to main loop

        # Start the first iteration immediately
        handle_iteration()

    def update_timer_text(self):
        if self.timer_count <= 10 and self.notExit:
            self.ui.ingame_timer.setText(f'Time left: {10 - self.timer_count} seconds')
            self.timer_count += 1
        else:
            self.timer.stop()



    def Clear_local_Data(self):
        for player in range(len(self.Local_Data)):
            self.Local_Data[player]['rolls'] = []
            self.Local_Data[player]['current_bet'] = ''

        print(self.Local_Data)

    def generate_dice(self):
        dice_list = []
        total_dice = 0

        for dice in range(0, self.total_dice_amount):
            dice_list.append(random.randint(1, 6))

        for dice in dice_list:
            total_dice += dice

        return dice_list, total_dice




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())