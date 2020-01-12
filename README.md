# Automated File Management

Automated file categorization and management using Python.
#### SortDownloads
- Runs on startup, sorts and organizes Downloads folder.
#### BackupVideos
- Runs on startup, moves all videos from \Videos to External drive
- Removes empty folders from \Videos

## Todo
- [x] Create configuration file
- [x] Create installer
- [x] Message box popup vs Win10 toasts
- [ ] Customization (Notification type, timing, etc)
- [ ] Option to skip x number of startups

## Possible Future Features
- [x] GUI for customization
- Dynamically add new file extensions to search for
- Dynamically add new folders for organization

## Configuration
- config.json file is located in ~\AppData\Roaming\Automated-File-Manager
- Default config gets created on app startup if no config file already exists

## Building
1.) Ensure pyinstaller is installed:
```
pyinstaller --version
```
2.) Run the following command in the main directory:
```
pyinstaller --noconsole --onefile Scripts\AutoFileManage.py
```
3.) Locate AutoFileManage.exe in the \dist\ folder

4.) For ideal results place a shortcut of the .exe in Windows startup folder
