# Locally-Hosted Roller Game ("Roll to 26")

A locally-hosted (LAN) multiplayer dice game built with **Python + PySide2**.
The project is split into two parts:

- **Servers** (`Server/`) — a login server and a game server. Both speak UDP and
  advertise themselves on the local network through broadcast discovery, so
  clients find them automatically.
- **Clients** (`user/`) — a PySide2 login window (`user/login/login.py`) that,
  after a successful login, launches the game window (`user/game.py`).

The `client.py` file at the repo root is the networking layer used by the game
client (UDP requests/responses to the game server).

> Platform note: the client uses [`pycaw`](https://pypi.org/project/pycaw/) for
> Windows audio control, so the **client side is Windows-only**. The servers
> themselves should run on any OS with Python, but they have only been tested
> on Windows.

---

## 1. Prerequisites

- Windows 10/11 (for the client)
- Python 3.10+ recommended
- All machines (server host + each player) must be on the **same LAN / subnet**
  so UDP broadcast discovery works.
- Local firewall must allow inbound UDP on:
  - **12345** (game server)
  - **65535** (login server)
  - A random ephemeral port chosen per client for game updates (the client
    binds one at startup)

## 2. Project layout

```
locally-hosted-roller-game/
├── client.py                 # Game client networking helpers
├── requirements.txt
├── .env.example              # Template for the shared secret keys
├── Server/
│   ├── login_server.py       # UDP login server (port 65535)
│   ├── game_server.py        # UDP game server (port 12345)
│   ├── admin_login_server_data.json   # User accounts (auto-managed)
│   └── admin_server_list.json         # Active game lobbies (auto-managed)
├── user/
│   ├── game.py               # Main game window
│   ├── game_ui.py            # Generated PySide2 UI
│   ├── volumeMixer.py
│   └── login/
│       ├── login.py          # Login window (launches game.exe on success)
│       └── login_ui.py
└── dist/                     # Prebuilt PyInstaller executables (optional)
    ├── game.exe
    ├── Roll to 26.exe
    └── login/
        └── login.exe
```

## 3. Setup (from source)

### 3.1 Create a virtual environment and install dependencies

From the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 3.2 Configure the shared secret keys

Both servers and clients read five shared keys from a `.env` file (see
`.env.example`). They act as simple "request type" identifiers — the **server
host and every client must use the exact same values**.

Create a file named `.env` in the repo root:

```env
SV_REQUEST_KEY=view_servers_key
SV_CREATE_KEY=create_server_key
SV_JOIN_KEY=join_server_key
SV_LEAVE_KEY=leave_server_key
SV_INSTRUCTION_KEY=instruction_key
```

Pick whatever strings you like — just make sure every machine uses the same
`.env`. (`USER_NAME` is written automatically by the login client after a
successful login, so you do not need to set it by hand.)

## 4. Running the servers

Run the servers on **one machine** on the LAN — this is the "host" machine.
Open two terminals (or run them as background processes).

### 4.1 Start the login server

```powershell
cd Server
python login_server.py
```

Expected output:

```
LOGIN SERVER IS RUNNING - LISTENING FOR LOGIN: ADDRESS <host-ip>
```

This binds to **UDP 65535** and answers `DISCOVER_LOGIN_IP` broadcasts.

### 4.2 Start the game server

In a second terminal:

```powershell
cd Server
python game_server.py
```

Expected output:

```
HH:MM AM/PM [GAME SERVER]  Server IP address: <host-ip>
HH:MM AM/PM [GAME SERVER]  GAME SERVER IS RUNNING - LISTENING FOR USERS AND DISCOVERY
```

This binds to **UDP 12345** and answers `DISCOVER_SERVER_IP` broadcasts. On
startup it also resets `admin_server_list.json` (the lobby list) to `[]`.

> Tip: leave both terminals open. All login attempts and lobby actions are
> printed there.

## 5. Running the clients

On each player's machine (must be on the same LAN as the server host):

1. Copy/clone the repository (or at least the `user/`, `client.py`, and `.env`
   files) onto the client machine.
2. Create a venv and `pip install -r requirements.txt` as in step 3.1.
3. Make sure `.env` exists at the repo root with the **same keys** as the
   server host.

### 5.1 Launch the login client

```powershell
cd user\login
python login.py
```

The window will:

1. Broadcast `DISCOVER_LOGIN_IP` to find the login server.
2. Let you log in or create an account.
3. On success, write `USER_NAME` into `.env` and try to launch `game.exe` (the
   PyInstaller build of `user/game.py`) from the same directory as the Python
   interpreter / login executable.

### 5.2 Launching the game directly (skip login during dev)

If you just want to test the game UI without going through login each time,
you can run it directly. Make sure `USER_NAME` is set in `.env` first (or
hard-code one) and that the game server is reachable:

```powershell
cd user
python game.py
```

`client.py` will broadcast `DISCOVER_SERVER_IP`. If no game server is found
within 5 seconds it falls back to single-player mode ("Enjoy Single Player"
will be printed).

## 6. Running the prebuilt executables (no Python needed)

The `dist/` folder contains a PyInstaller build:

- `dist/login/login.exe` — login window
- `dist/game.exe` — game window
- `dist/Roll to 26.exe` — combined / branded build

To use them as a player:

1. Place `login.exe` and `game.exe` **in the same folder** (the login
   executable launches `game.exe` from its own directory).
2. Put your `.env` file (with the shared keys) **next to the executables**.
3. Make sure the host machine is already running both `login_server.py` and
   `game_server.py`.
4. Double-click `login.exe`.

The servers themselves are not bundled — you still need to run
`login_server.py` and `game_server.py` from source on the host machine.

## 7. Typical end-to-end startup

On the **host** machine:

```powershell
cd Server
python login_server.py     # terminal 1
python game_server.py      # terminal 2
```

On each **player** machine:

```powershell
cd user\login
python login.py
```

Log in → the game window opens → create or join a lobby that shows up in the
server list → play.

## 8. Troubleshooting

- **"No server response. Relaunch Login When Server is Up"** — the login
  client could not find the login server via broadcast. Check that
  `login_server.py` is running on the LAN host, that you are on the same
  subnet, and that UDP 65535 is allowed through the firewall.
- **"No server response. Enjoy Single Player"** — same problem, but for the
  game server (UDP 12345).
- **Both clients on the same machine** — each client binds a random UDP port
  for game updates, so multiple clients on one machine should work, but only
  one process can bind UDP 12345/65535 at a time (the servers).
- **Account file resets / lobby weirdness** — `game_server.py` wipes
  `admin_server_list.json` on every startup. User accounts in
  `admin_login_server_data.json` are persistent.
- **`KeyError` on env vars in the client** — your `.env` is missing one of the
  five `SV_*_KEY` entries, or the client is being run from a directory where
  `python-dotenv` cannot find `.env`. Run the client from the repo root, or
  copy `.env` next to the script/executable.

## 9. Rebuilding the executables (optional)

PyInstaller spec files are included:

```powershell
pip install pyinstaller
cd user
pyinstaller game.spec
cd login
pyinstaller login.spec
```

Outputs land in each folder's `dist/` directory. Copy `login.exe` and
`game.exe` into the same folder before distributing.

## View Test Gameplay here
https://youtu.be/iw_uIJkBHSU
