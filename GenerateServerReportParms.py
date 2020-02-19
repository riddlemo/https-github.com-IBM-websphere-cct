#author Dennis Riddlemoser
import sys

print

mismatches = ['False','All']
titleSuffixes = ['with all attribute values','with attribute values that do not match only']
fileNameSufixes = ['','NotMatch']
reportNameSuffix = ['','NM']
for srv in sys.argv[1:]:
	idx = 0
	for mismatch in mismatches:
		print '%s%s:ReportType=Server' % (srv,reportNameSuffix[idx])
		print '%s%s:Title=%s Servers %s' % (srv,reportNameSuffix[idx],srv,titleSuffixes[idx])
		print '%s%s:Clusters:1=' % (srv,reportNameSuffix[idx])
		print '%s%s:Servers:1=.*::%s' % (srv,reportNameSuffix[idx],srv)
		print '%s%s:ReportList=All' % (srv,reportNameSuffix[idx])
		print '%s%s:ReportOnlyMismatched=%s' %(srv,reportNameSuffix[idx],mismatch)
		print '%s%s:FileName=%s%s' % (srv,reportNameSuffix[idx],srv,fileNameSufixes[idx])
		print
		idx = idx + 1
