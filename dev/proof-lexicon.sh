LEXC=$1
for line in `cat $LEXC | grep 'ADVINFL ; .*"' | sed 's/ /_/g' | sed 's/^! *//g'`; do 
	word=`echo $line | cut -f1 -d':' | sed 's/^! *//g' | iconv -f utf-8 -t iso-8859-9`;
	#wget -q -O - --referer "http://tdkterim.gov.tr/bts/arama/index.php" "http://tdkterim.gov.tr/bts/arama/?kategori=verilst&kelime=$word&ayn=tam"  | grep "$word" | grep -e "<i> a. bl.</i>" -e "<i> a. " -e "<i> a.</i>" > /dev/null
	wget -q -O - --referer "http://tdkterim.gov.tr/bts/arama/index.php" "http://tdkterim.gov.tr/bts/arama/?kategori=verilst&kelime=$word&ayn=tam"  | grep "$word" | grep -e "<i> zf.</i>" -e "<i> zf. " -e "<i> zf.</i>" > /dev/null
	echo $?" "$line;
	sleep 2
done
	
		
	

