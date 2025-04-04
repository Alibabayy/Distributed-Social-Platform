Distributed Social Platform
A local-first journaling application with optional remote publishing, enabling users to share posts or private messages over a custom DSP (Distributed Social Platform) server. Integrates external APIs (OpenWeather, Last.FM) for dynamic content insertion, and provides a Tkinter-based GUI for user-friendly interaction.

Features
Local Journaling
Write, edit, and view journal entries stored locally in custom profile files. Operates offline by default.

Remote Publishing (TCP Sockets + JSON Protocol)
Connects to a DSP server using a JSON-based protocol. Supports creating a new user, posting journal entries, and updating user bios.

Transclusion with 3rd-Party APIs
Utilizes the OpenWeather and Last.FM APIs to replace keywords like @weather or @lastfm with live data (e.g., current weather info, music details).

Direct Messaging
Extends the protocol to allow sending private messages (directmessage) to other DSP users, plus retrieval of “new” or “all” messages.

Tkinter GUI
Provides a chat-like interface with contact lists, conversation threading, auto-updating message polls, and a friendly user login/register flow.

Offline Access & Persistence
Caches messages, contacts, and profiles locally so users can review previously downloaded data even without an active internet connection.


Getting Started
Clone this repository:

bash
复制
编辑
git clone https://github.com/Alibabayy/Distributed-Social-Platform.git
cd Distributed-Social-Platform
Install dependencies

Python 3.9+ recommended

Additional libraries: requests, lxml, tkinter (built-in on most systems), etc.

If you’re using a requirements.txt, run:

pip install -r requirements.txt
Run the main app:

python a5.py
This should open the Tkinter interface. Fill in or load your profile, specify the DSP server address, and explore local journaling or direct messaging.

Usage
Local Journal: Write entries offline, stored in your local profile.

Publish: Post an entry to the DSP server or update your bio.

APIs: Use @weather or @lastfm within journal text to embed real-time data.

Direct Messages: Send private messages to other users (identified by username), retrieve conversation history, and browse them in the GUI.

Customizing / Configuration
Server Address
In Profile.py (or wherever you store user data), you can edit the dsuserver value to point to the actual DSP server IP/port.

API Keys

OpenWeather: store your API key in OpenWeather.py or pass it at runtime.

Last.FM: similarly, store or pass your Last.FM API key.


Contributing
Fork this repo & create a new branch for your feature or bugfix.

Make commits with clear, concise messages.

Submit a Pull Request detailing changes made.

License
This project is for educational use under the MIT License. Feel free to adapt for your own learning or portfolio.

Acknowledgements
ICS32: Base specification and DSP server environment.

OpenWeather: Weather data API.

Last.FM: Music data API.

Tkinter: Python’s built-in GUI framework.

