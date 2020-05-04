# bglugwatch v.0.2.11-wip
# copyright (c) 2019-2020 ittussarom retals mail ynohtna
# BGLUGwatch is licensed under the GNU GPLv3 or later, a copyleft license.
# copyleft states that it is illegal to switch to a different license without the explicit permission of TheTechRobo
# you should have received a copy; else go to https://github.com/thetechrobo/bglugwatch-cleanslate/blob/master/LICENSE
# END OF NOTICES
# import necessary modules
import tkinter
from tkinter import Button, Label, Text, Menu, ttk
from tkinter import messagebox as msg
from tkinter import *
import subprocess
from sys import exit
import webbrowser
from tkinter.ttk import * #so that all widgets use themes
# set up window
main = tkinter.Tk()
menubar = Menu(main)
main.title("BGLUGwatch")
s = ttk.Style()
s.theme_use('clam')
# DECLARING
def uc(): #source stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output/9266901#9266901
    msg.showinfo("Attempting to update...", "Please wait while git does its job.")
    output = subprocess.Popen(["git pull"],stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) #Prepare the git pull
    response = output.communicate() #run git pull and get the output
    if response == (b'Already up to date.\n', None):
        print("Already up to date.")
        msg.showinfo("Already up to date.", "You can use BGLUGwatch freely!")
    elif response == (b'Already up-to-date.\n', None):
        print("Already up-to-date.")
        msg.showinfo("Already up to date.", "You can use BGLUGwatch freely!")
    elif response == (b'Already up to date.\n', b''):
        print("Already up to date.")
        msg.showinfo("Already up to date.", "You can use BGLUGwatch freely!!")
    elif response == (b'Already up-to-date.\n', b''):
        msg.showinfo("Already up-to-date.", "You can use BGLUGwatch freely!")
    elif response == (b'', b'fatal: not a git repository (or any of the parent directories): .git\n'):
        print(response)
        msg.showerror("Error!", "There was an error updating BGLUGwatch.")
    elif response == (b'', b'fatal: not a git repository: .git\n'):
        print(response)
        msg.showerror("Error!", "There was an error updating BGLUGwatch.")
    else:
        print(response)
        msg.showinfo("Updated!", "BGLUGwatch will now exit, please restart it.")
        exit()
def clist(winname): #create list & scrollbar
    scrollbar = Scrollbar(winname) #add scrollbar
    scrollbar.pack(side=RIGHT, fill=Y) #pack scrollbar
    mylist = Listbox(winname, yscrollcommand=scrollbar.set)#create list
    return mylist #return list
def hello():
    win = Toplevel()
    win.title('About BGLUG and the program')
    # create child window
    # display message
    mylist = clist(win) #create list & scrollbar
    def insert(string):
        mylist.insert(END, string)
    insert("The Bruce Grey Linux Users Group (BGLUG) was founded in 2000 to bring local Linux users together and to help newcomers to Linux.")
    insert("The group holds monthly meetings, gives technical presentations, distributes Linux CD-ROMs and hosts a web site, www.bglug.ca, which provides online support.")
    insert("The Bruce-Grey Linux Users Group is currently centered in Owen Sound, but has members scattered around Bruce and Grey counties. The group is freely open to everyone.")
    insert("We gather together for four main reasons:")
    insert("advocacy, education, support, and socializing.")
    insert("")
    insert("Bruce Grey Linux User's Group was originally founded by Richard Court in early 2000. Richard Court, Brad Rodriguez, Andrew Howlett ")
    insert("and Dan Eriksen have been key members since its creation.")
    insert("Richard has given up control of BGLUG to the current active maintainer, Dan Eriksen (site admin, LPIC-1 certified).")
    insert("A lot of work is still from the other members of the group, namely Andrew Howlett (meeting coordinator, LPIC-1 certified) who started our free CDs service.")
    insert("Over the last few years we have seen the group grow significantly in size. Nearly everyone has played a role in making the meetings interesting")
    insert("and helping to keep the group going.")
    insert("The bglug.ca domain was purchased in November 2002. After several months, the forums were added and then eventually our own mailing list.")
    insert("We are constantly evolving and gladly welcome any constructive feedback and suggestions. If you have any thoughts about the group, please let us know!")
    insert("")
    insert("BGLUGwatch v.0.2.10-stable, copyright (c) Ittussarom Retals Mail Ynohtna. Licensed under the GNU GPLv3.")
    insert("Find me on GitHub at: www.github.com/thetechrobo/bglugwatch-cleanslate")
    insert("Thanks for using!")
    mylist.pack(fill = BOTH)
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    Button(win, text='OK', command=win.destroy).pack()
    win.minsize(1100, 100)
def showMessageTwo(): #Message two
    print("Showing message two, if anyone's listening......")
    m2 = Toplevel() #create window
    m2.title("Message 1")
    mylist = clist(m2)
    def insert(string):
        mylist.insert(END, string)
    insert("Message from LP")
    insert("")
    insert("I just got the word 'All LUG meetings at the United Way are cancelled until further notice' Chris.")
    insert("Sent from ProtonMail <protonmail.ch>, encrypted email based in Switzerland.")
    insert("")
    insert("Reply from TtR")
    insert("")
    insert("Well, I'm sad, but it was bound to happen.")
    insert("Sent from TtR's iPhone 4")
    insert("")
    insert("Reply from Brad Rodriguez")
    insert("")
    insert("I have updated the web page to show this.")
    insert("")
    insert("- Brad")
    insert("")
    insert("Reply from Logan Streondj")
    insert("How about we meet on Jitsi (open-source video chat)")
    insert("https://meet.jit.si/bglug")
    Button(m2, text="OK", command=m2.destroy).pack()
    m2.minsize(750, 100)
    mylist.pack(fill=BOTH)
def ShowMessageOne(): #message one
    print("Showing messages...")
    m1 = Toplevel()
    mylist = clist(m1)
    def insert(string):
        mylist.insert(END, string)
    insert("Message from LP")
    insert("")
    insert("Hi all, ")
    insert("I hope everyone is well, I have been thinking about you all.")
    insert("Chris")
    insert("")
    insert("Sent from ProtonMail, encrypted email based in Switzerland.")
    m1.title(':(')
    mylist.pack(fill=BOTH)
    Button(m1, text="OK", command=m1.destroy).pack()
    m1.minsize(400, 250)
def subshelp():
    win = Toplevel()
    win.title('Under Construction')
    Label(win, text="Under construction").pack()
def contrib():
    webbrowser.open("https://github.com/thetechrobo/bglugwatch-cleanslate", new=1) # SOURCE: gist.github.com/RandomResourceWeb/93e887facdb98937ab5d260d1a0df270
# Tabs (source www.djangocentral.com/creating-tabbed-widget-with-python-for-gui-application/)
#Create Tab Control
TAB_CONTROL = ttk.Notebook(main)
#Tab1
TAB1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='Next meeting')
#Tab2
TAB2 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='Articles')
#Tab3
TAB3 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB3, text='Mailing list')
#TAB4
TAB4 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB4, text='Update cache')
TAB_CONTROL.pack(expand=1, fill="both")
#For tab 1
def moreinfomeeting():
    # create child window
    more = Toplevel()
    more.title('Online Jitsi meeting May 5, 2020')
    # display message
    message = '''The next BGLUG meeting has been proposed:
    Meet on Jitsi (open-source video chat) at: https://meet.jit.si/bglug on: May 5 @ 7pm.
    Topic: Features of Jitsi, presentations welcome! (Propose a presentation on the mailing list.)
    See you there!'''
    Label(more, text=message).pack()
    Button(more, text="OK", command=more.destroy)
ttk.Label(TAB1, text="Meet on https://meet.jit.si/bglug 1st Tuesday of May @ 7pm").pack()
ttk.Button(TAB1, text="More info...", command=moreinfomeeting).pack()
#For tab 2
def abtlin():
    abtlin = Toplevel()
    abtlin.title('About GNU/Linux')
    linux = '''GNU/Linux ("Linux") is a clone of the operating system Unix. It was originally created by Linus Torvalds with the assistance of
    thousands of volunteer developers around the world. It is distributed under the GNU General Public License which means the source code is
    freely available to everyone. Linux has powered much of the Internet for years, and is now available with many applications for "desktop" computer users.'''
    ttk.Label(abtlin, text=linux).pack()
def showspec1():
    specs = Toplevel()
    specs.title("Truncated specs (scroll for more)")
    #SOURCE: https://stackoverflow.com/questions/50625306/whats-the-best-way-to-show-data-which-should-be-in-a-table-using-tkinter-python and https://stackoverflow.com/questions/47515014/how-do-i-use-tkinter-treeview-to-list-items-in-a-table-of-a-database
    #Create table
    scrollbar = Scrollbar(specs) #add scrollbar
    scrollbar.pack(side=RIGHT, fill=Y) #pack scrollbar
    tree = ttk.Treeview(specs, yscrollcommand=scrollbar.set)
    tree["columns"] = ["Email client", "Sylpheed", "Mozilla", "Balsa", "Evolution"]
    tree["show"] = "headings"
    tree.heading("Email client", text="Email client")
    tree.heading("Sylpheed", text="Sylpheed")
    tree.heading("Mozilla", text="Mozilla")
    tree.heading("Balsa", text="Balsa")
    tree.heading("Evolution", text="Evolution")
    def ins(stuffs):
        tree.insert("", 99, values=stuffs)
    tree.pack()
    ins(("Multiple accounts?", "yes", "yes", "yes", "yes"))
    ins(("Filter criteria", "headers", "headers/body", "headers/body", "header/body/attach/size/regex"))
    ins(("(does/does not)", "contain regex", "contain/is/begin/end", "contain regex", "contain/is/begin/end"))
    ins(("Multiple filters?", "2 and/or", "N and/or", "N and/or", "N and/or"))
    ins(("Filter actions", "Move/delete", "move/delete/flag/label", "move/delete/prog'md action", "move/delete/colour"))
    ins(("Import Eudora mailbox?", "yes", "yes", "yes", "yes"))
    ins(("Import Eudora addresses?", "no", "yes", "?", "?"))
    ins(("Import Eudora filters?", "no", "?", "?", "?"))
    ins(("PGP?", "yes", "yes", "?", "yes"))
    ins(("Attachments?", "yes", "yes", "yes", "yes"))
    ins(("Return receipts?", "no", "yes", "yes", "no"))
    ins(("BCC?", "yes", "yes", "yes", "yes"))
    ins(("Message size limit?", "yes", "yes", "no", "no"))
    ins(("Signature files?", "one", "one per account", "multiple", "one per account"))
    ins(("Address books?", "multiple", "multiple", "multiple", "multiple"))
    ins(("Message labels?", "no", "yes (5)", "no", "no, but can flag messages"))
    ins(("HTML email?", "no", "optional", "no", "optional"))
    ins(("External actions?", "yes", "no", "filter", "no"))
    Button(specs, text="OK", command=specs.destroy).pack()
def article1():
    article1 = Toplevel()
    article1.title("Choosing a suitable email client")
    mylist = clist(article1)
    def insert(string):
        mylist.insert(END, string)
    insert("Well, for better or worse, I've chosen an email client. You'll recall that I had narrowed it down to four")
    insert("possibles, based upon the rather modest requirements that the client support multiple email accounts and")
    insert("have some filtering capabilities. So I installed all four, and I started looking at them, keeping in mind the")
    insert("features of Eudora that I use every day or really like. ")
    Button(article1, text="View truncated spec list", command=showspec1).pack()
    insert("==================================COMMENTARY========================================================")
    insert("")
    insert("Evolution has the most flexible filtering -- except that Balsa allows the use of an external program as a")
    insert("filter, which would be VERY nice for some of the spam filtering software I've seen. But all are as good as")
    insert("Eudora 3. (All but Mozilla have some support for regular expressions.)")
    insert("")
    insert("I'm thinking that I'll be using PGP more in the future, so that's important. I also send and receive messages")
    insert("with \"return receipts\" so I'd like the client to handle that.")
    insert("A VERY important feature is the ability to leave a message on the server if it exceeds a certain size. I'm on")
    insert("a dialup line, and the occasional unwanted 2.5MB message does appear. It also keeps a lot of Klez viruses")
    insert("away. This is a \"deal breaker\" and is sufficient to disqualify Balsa and Evolution.")
    insert("Another Eudora feature I use a lot is the ability to give messages color-coded labels. Only Mozilla offers")
    insert("this. (Evolution lets you \"flag\" a message, which is like having one label, but I use at least four.) Of the four,")
    insert("only Mozilla offers this.")
    insert("I do NOT want HTML email...what's important to me is that the feature can be turned off, and the client")
    insert("forced to use text email. All four pass this test.")
    insert("So, the best match to my desired feature set is Mozilla. Sylpheed is a close second. Sylpheed is probably")
    insert("the closest to Eudora in appearance, although none of the four offers the Eudora user interface that I've come")
    insert("to love, with multiple mailboxes and multiple messages open simultaneously. Balsa is ok, and I frankly dislike")
    insert("the Evolution look and feel and its excess baggage.")
    insert("On the other hand, I may be unusual among Linux users in that I *like* a combined email-news-browser")
    insert("program like Mozilla. I've had a lot of problems in the Windoze environment getting my email to work with my")
    insert("browser and news reader. (If I didn't like Eudora so much, I might have switched to Netscape mail long ago.)")
    insert("")
    insert("The new user interface will take some getting used to, and I'll miss some handy features. But until")
    insert("someone brings out Eudora for Linux, it's a price I'm willing to pay.")
    mylist.pack(fill=BOTH)
    Button(article1, text="OK", command=article1.destroy).pack()
    article1.minsize(755, 50)
def article2():
    article2 = Toplevel()
    article2.title("Win4Lin review")
    mylist = clist(article2)
    def insert(string):
        mylist.insert(END, string)
    insert("Working")
    insert("on it...")
    mylist.pack(fill=BOTH)
    Button(article2, text="OK", command=article2.destroy).pack()
def Articles():
    articles = Toplevel()
    articles.title('Articles')
    Label(articles, text="Select an article.")
    Button(articles, text="December 23, 2002: Choosing a suitable mail client.", command=article1).pack()
    Button(articles, text="February 11, 2003: Win4Lin review", command=article2).pack()
ttk.Button(TAB2, text="About Linux", command=abtlin).pack()
ttk.Button(TAB2, text="Archived articles", command=Articles).pack()
#For tab3.
ttk.Label(TAB3, text="Newest Mail on the Mailing List").pack()
ttk.Label(TAB3, text='''FROM: LP
SUBJECT: All LUG Meetings are Cancelled until further notice !
"I just got the word..."''').pack()
ttk.Button(TAB3, text="Read", command=showMessageTwo).pack()
ttk.Label(TAB3, text='''FROM: LP
SUBJECT: I hope everyone is well!
"Hi all,..."''').pack()
ttk.Button(TAB3, text="Read", command=ShowMessageOne).pack()
ttk.Label(TAB3, text='''
For messages direct to your mailbox, go to http://bglug.ca/mailman/listinfo/group_bglug.ca and sign
up for the mailing list!''').pack()
#TAB4
ttk.Button(TAB4, text="Update cache", command=uc).pack()
ttk.Label(TAB4, text="This button will update the cache of BGLUGwatch. It will not work if you didn't git clone the repo as it requires the .git subfolder. So, if you didn't clone the repo, don't touch this.").pack()
# MENUBAR
# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="About...", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit BGLUGwatch", command=main.quit)
menubar.add_cascade(label="BGLUGwatch", menu=filemenu)
# create another pulldown menu, and add IT to the menu bar
viewmnu = Menu(menubar, tearoff=0)
viewmnu.add_command(label="About box", command=hello)
viewmnu.add_command(label="Next meeting", command=moreinfomeeting)
viewmnu.add_command(label="Articles", command=Articles)
viewmnu.add_separator()
viewmnu.add_command(label="Exit BGLUGwatch", command=main.quit)
menubar.add_cascade(label="View", menu=viewmnu)
utilmnu = Menu(menubar, tearoff=0)
utilmnu.add_command(label="Update BGLUGwatch", command=uc)
utilmnu.add_command(label="Contribute!", command=contrib)
utilmnu.add_separator()
utilmnu.add_command(label="Exit BGLUGwatch", command=main.quit)
menubar.add_cascade(label="Utilities", menu=utilmnu)
# display the menu
main.config(menu=menubar)
# show message on launch
msg.showinfo("Online meeting May 5, 2020 @ 7pm", "There is a meeting this month, see more details by clicking `More info...' inside the `Next meeting' tab (the first one)")
main.mainloop()
