chromedriver.py
===============

Chromedriver's download script.

	$ python chromedriver.py path/to/install
	WARNING:root:fetching new 2.9 version of chromedriver
	WARNING:root:trying url http://chromedriver.storage.googleapis.com/2.9/chromedriver_linux64.zip
	WARNING:root:release notes: http://chromedriver.storage.googleapis.com/2.9/notes.txt
	WARNING:root:----------ChromeDriver v2.9 (2014-01-31)----------
	Supports Chrome v31-34
	Resolved issue 665: Use /data/local/tmp for command line flags on user builds [OS-Android, Pri-0]
	Resolved issue 696: Return window handle to App window (like Google Keep) in command driver.getWindowHandles [Pri-0]
	Resolved issue 694: Update http://chromedriver.storage.googleapis.com/LATEST_RELEASE for users to query for latest release and do automatic update in script [Pri-0]
	Resolved issue 690: Fix clicking on Map Area [Pri-0]
	Resolved issue 454: chromedriver didn't support Debian 7 [Pri-0]
	Resolved issue 638: chomedriver.exe 2.6 to 2.8 built on Win7 build bot always produce empty chromedriver.log on local windows machine. [Pri-0]
	Resolved issue 672: Wait 60 seconds for chrome to start up on all OS and 30 seconds for chrome shutdown on Mac and Linux. [Pri-0]
	Resolved issue 660: Port used for android adb forward leaks. [Pri-0]
	Resolved issue 676: LaunchApp method for launching Chrome apps using their ID [OS-All, Pri-0]


	WARNING:root:done

	$ python chromedriver.py path/to/install
	WARNING:root:current version of chromedriver is already installed
