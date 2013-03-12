ccdcSalesReportsDir="C:\\Users\\Chad\\Downloads\\"
ccdcSalesReportJan=ccdcSalesReports + "Catoctin Creek Sales"
ccdcSalesReportJancsv=file(ccdcSalesReportJan,'w')
for 'Premises,' in ccdcSalesReportJancsv:
	file.write('1/31/2013,Closed Won,')
file.readline(ccdcSalesReportJancsv)

file.close(ccdcSalesReportJancsv)

