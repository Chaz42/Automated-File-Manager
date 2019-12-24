# Automated File Management

Automated file categorization and management using Python.
#### SortDownloads
- Runs on startup, sorts and organizes Downloads folder.
#### BackupVideos
- Runs on startup, moves all videos from \Videos to External drive
- Removes empty folders from \Videos

## Todo
- [ ] Create configuration file
- [ ] Dynamically create .cmd file based on script locations
- [ ] Create installer
- [ ] Message box popup vs Win10 toasts
- [ ] Customization (Notification type, timing, etc)

## Possible Future Features
- GUI for customization
- Dynamically add new file extensions to search for
- Dynamically add new folders for organization

## Installing
1.) Win + R

2.) Type 'shell:startup', hit enter

3.) Create empty .cmd file

4.) Enter the following, change path to script locations

```
python C:\folder\BackupVideos.py
python C:\folder\SortDownloads.py
```
