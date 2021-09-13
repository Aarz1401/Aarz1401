import pyperclip,sys
if len(sys.argv)<2:
    print("No argument")
    sys.exit()
pyperclip.copy("hello, world"*int(sys.argv[1]))
print("Hello world has been copied to your clipboard")
