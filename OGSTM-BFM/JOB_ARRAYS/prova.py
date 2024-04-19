startTime=0
endtime=86400 * 30
pChkptFreq=endtime

filein="data.template"
fileout="data.prova"
f = open(filein,'r')
filedata = f.read()
f.close()

f = open(fileout,'w')
newdata = filedata.replace("@startTime",str(startTime))
newdata = newdata.replace("@endtime",str(endtime))
newdata = newdata.replace("@pChkptFreq",str(pChkptFreq))
f.write(newdata)
f.close()

