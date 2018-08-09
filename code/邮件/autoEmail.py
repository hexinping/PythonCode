#_*_ coding:utf-8 _*_
#http://www.myexception.cn/perl-python/1175877.html
#一个python的邮件发送脚本，自动，定时，可以附件发送，抄送，附有说明文件

import datetime
import smtplib
import os,sys
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from optparse import OptionParser

EMAILHOME=sys.path[0]

#sender name and password
senderName = ""
senderPass = ""

#list of all receiver
receiverList =[]
receiverTmpList = []
receiverCCTmpList = []


#get the username and pasword
def getUserAndPass(senderFile):
	f=open(senderFile)
	username=f.readline()
	password=f.readline()
	f.close()
	return (username.strip(os.linesep),password.strip(os.linesep))

#get the receiver list
def getReceiverList(fileName):
	rev = open(fileName)
	content = rev.readlines()
	rev.close()

	for x in range(len(content)):
		content[x]=content[x].strip().strip(os.linesep)

	while '' in content:
		content.remove('')
	return (content)


#get content of the mail
def getContent(fileName):
	contentTmp=''
	if os.path.exists(fileName):
		contentF = open(fileName)
		contentTmp = contentF.read()
		contentF.close()
	return contentTmp



#parameters process
parser = OptionParser()


parser.add_option('-s', '--sender', dest='sender',
        help='file for sender of the mail', default=None)
parser.add_option('-r', '--receiver', dest='receiver',
        help='list file for receivers of the mail',default=None)
parser.add_option('-p', '--cc', dest='cc',
        help='list file for receivers of carbon copy', default=None)
parser.add_option('-t', '--title', dest='title',
        help='title of the email,string', default='Auto email') # 可以自定义修改主题
parser.add_option('-c', '--content', dest='content',
        help='content of the mail,must be a file',default=None)
parser.add_option('-a', '--attach', dest='attach',
        help='attachment of the file',default=None)
parser.add_option('-n', '--nameattach', dest='nameattach',
        help='name for attachment of the file',default=None)
parser.add_option('-l', '--server', dest='server',
        help='log in to the server',default='smtp.126.com') # 可以修改邮件服务器
parser.add_option('-i', '--info', dest='info',
        help='information of the content,string,but not file',default='Auto email')
parser.add_option('-f', '--form', dest='form',
        help='form of the content,html or plain',default='plain')


(options, args) = parser.parse_args()


#get sender infor
if not options.sender:
	if os.path.exists(EMAILHOME+r'/sender.list'):
		(senderName,senderPass)=getUserAndPass(EMAILHOME+r'/sender.list')
		if senderName.strip()=="" or senderPass.strip()=="":
			print "no sender!"
			exit(0)
	else:
		 print "no sender!"
		 exit(0)
else:
	 if os.path.exists(options.sender):
	 	 (senderName,senderPass)=getUserAndPass(EMAILHOME+r'/sender.list')
	 	 if senderName.strip()=="" or senderPass.strip()=="":
	 	 	print "no sender!"
	 	 	exit(0)
	 else:
	 	print "the file for sender list does not exists!"
	 	exit(0)


#get list of all receiver
if not options.receiver:
	if os.path.exists(EMAILHOME+r'/receiver.list') or os.path.exists(EMAILHOME+r'/receivercc.list'):
		if os.path.exists(EMAILHOME+r'/receiver.list'):
		 	receiverTmpList= getReceiverList(EMAILHOME+r'/receiver.list')
		if os.path.exists(EMAILHOME+r'/receivercc.list'):
		 	receiverCCTmpList= getReceiverList(EMAILHOME+r'/receivercc.list')

		receiverList=receiverTmpList+receiverCCTmpList
		if len(receiverList)==0:
			print "no receiver!"
			exit(0)
	else:
		print "no receiver list file!"
		exit(0)
else:
	if os.path.exists(options.receiver) or os.path.exists(options.cc):
		if os.path.exists(options.receiver):
			receiverTmpList= getReceiverList(options.receiver)
		#if os.path.exists(options.cc):
		receiverCCTmpList= getReceiverList(options.receiver)

		receiverList=receiverTmpList+receiverCCTmpList
		if len(receiverList)==0:
			print "no receiver from the list file!"
			exit(0)
	else:
		print "receiver list file does not exist!"
		exit(0)


if options.attach and not options.nameattach:
	print "give a name to the attachment!"
	exit(0)

#make a mail    
mailall=MIMEMultipart()

#content of the mail 
if options.content:
	mailcontent =getContent(options.content)
	mailall.attach(MIMEText(mailcontent,options.form,'utf-8'))
elif options.info:
	mailcontent = str(options.info)
	mailall.attach(MIMEText(mailcontent,options.form,'utf-8'))


#attachment of the mail   
if options.attach:
    mailattach =getContent(options.attach)
    if mailattach !='':
        contype = 'application/octet-stream'
        maintype,subtype=contype.split('/',1)
        attfile=MIMEBase(maintype,subtype)
        attfile.set_payload(mailattach)
        attfile.add_header('Content-Disposition','attachment',options.nameattach)
        print "attach file prepared!"
        mailall.attach(attfile)


#title,sender,receiver,cc-receiver,
mailall['Subject']=options.title
mailall['From']=senderName
mailall['To']=str(receiverTmpList)
if len(receiverCCTmpList) !=0:
    mailall['CC']=str(receiverTmpList)

#get the text of mailall
fullmailtext=mailall.as_string()
print(fullmailtext)
print "prepare fullmailtext ok."

mailconnect = smtplib.SMTP(options.server)
try:
	 
	 mailconnect.login(senderName,senderPass)
   
except Exception,e:
    print "error when connect the smtpserver with the given username and password !"
    print e
    exit(0)


print "connect ok!"



try:
    mailconnect.sendmail(senderName, receiverList, fullmailtext)
except Exception,e:
    print "error while sending the email!"
finally:
    mailconnect.quit()


print 'email to '+str(receiverList)+' over.'


