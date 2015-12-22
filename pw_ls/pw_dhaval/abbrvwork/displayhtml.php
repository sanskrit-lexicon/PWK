<?php
/* Usage
php displayhtml.php abbrvoutput/sortedcrefsiast.txt abbrvoutput/display.html 1
*/
//error_reporting(0);
$header = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
      <style>
         table.fixed {table-layout:fixed; width:100%; border:1px solid black;}/*Setting the table width is important!*/
         td.zero {width:50px; border:1px solid black; text-overflow:ellipsis; }
         td.one {width:200px; border:1px solid black; text-overflow:ellipsis; padding: 10px;}
         td.two {width:200px; border:1px solid black;text-overflow:ellipsis; padding: 10px;}
         td.three {width:100px; border:1px solid black;text-overflow:ellipsis; padding: 10px;}
         td.four {width:100px; border:1px solid black;text-overflow:ellipsis; padding: 10px;}
		 td {overflow:scroll;}
      </style>
<!--... Defining UTF-8 as our default character set, so that devanagari is displayed properly. -->
<meta charset="UTF-8">
</head> 
<body>
';
$in = $argv[1];
$out = $argv[2];
$topcontent = $argv[3];
$file = fopen($out,'w+');
fputs($file,$header);
// Code to arrange the sortedcrefsiast.txt in HTML with links to dictionaries for testing.
$input = file($in);
$dictionaryname=array("ACC","CAE","AE","AP90","AP","BEN","BHS","BOP","BOR","BUR","CCS","GRA","GST","IEG","INM","KRM","MCI","MD","MW72","MW","MWE","PD","PE","PGN","PUI","PWG","PW","SCH","SHS","SKD","SNP","STC","VCP","VEI","WIL","YAT");
$hrefyear = array("2014","2014","2014","2014","2014","2014","2014","2014","2014","2013","2014","2014","2014","2014","2013","2014","2014","2014","2014","2014","2013","2014","2014","2014","2014","2013","2014","2014","2014","2013","2014","2013","2013","2014","2014","2014");

$srno = 1;
$top1 = "<h1>PW - Abbreviations for checking.</h1><p>Note - Check the links and see whether the reference is correct or false. <br/>Open finalabbrv.txt file. When the reference is incorrect, correct the AS data i.e. the first entry before '@'. If the reference is correct, place a ';' before it.</p><p>We would separate those entries into change.txt and nochange.txt by `postprocess.py`.</p><p>Please see <a href='https://github.com/sanskrit-lexicon/CORRECTIONS/tree/master/pw_dhaval'>this</a> for the code and readme.</p><table>";
$top2 = "<h1>PW - Literary resources</h1><p>Note - Check the links and see whether the reference is correct or false. <br/>Copy paste the content of cbisub.txt or cmbsub.txt to some file and save it. Open that file. Correct the readings in that file as per <a href='https://github.com/sanskrit-lexicon/CORRECTIONS/issues/146#issuecomment-163463468'>Standard Convention</a><table> and submit on <a href='https://github.com/sanskrit-lexicon/PWK/issues'>PWK repository</a>";
if ($topcontent==='1') {
	fputs($file,$top1);	
}
elseif ($topcontent==='2') {
	fputs($file,$top2);
}
for ($i=0;$i<count($input);$i++)
{
	if ($topcontent==='1') {
	decoratehtml($input[$i],$file,"PW");
	}
	elseif ($topcontent==='2') {
	decoratehtml1($input[$i],$file,"PW");
	}
	$srno++;
}
fputs($file,"</table></body></html>");
fclose($file);

# To decorate strings such as `Âapst@A7APST@rAD@rAD@93808@1`
# Expected outputs are Sr.no - L no. - IAST - AS - key1 - count.
# IAST to link to digital edition
# AS to link to PDF.
function decoratehtml($text,$file,$dict)
{
	global $srno;
	list($iast,$as,$key1,$key2,$lnum,$count) = explode('@',$text);
	fputs($file,'<tr><td class="zero">'.$srno.'</td><td class="zero">'.$lnum.'</td><td class="one">'.$as.'</td><td class="one">'.weblink($dict,$key1,$iast).'</td><td class="three">'.pdflink("PW",$key1).'</td><td class="three">'.$key2.'</td><td class="zero">'.$count.'</td></tr>');
}
function decoratehtml1($text,$file,$dict)
{
	global $srno;
	$split = preg_split('/[@:]/',$text); 
	$as = $split[0];
	$key1 = $split[1];
	$key2 = $split[2];
	$lnum = $split[3];
	fputs($file,'<tr><td class="zero">'.$srno.'</td><td class="zero">'.$lnum.'</td><td class="one">'.$as.'</td><td class="one">'.weblink1($dict,$key1).'</td><td class="three">'.pdflink("PW",$key1).'</td></tr>');
}
function pdflink($dict,$word)
{
	return '<a href="http://www.sanskrit-lexicon.uni-koeln.de/scans/awork/apidev/servepdf.php?dict='.$dict.'&key='.$word.'" target="_blank">'.$word."</a>";
}
function weblink($dict,$inputword,$ref)
{
	$y=Cologne_hrefyear($dict);
	return '<a href="'."http://www.sanskrit-lexicon.uni-koeln.de/scans/".$dict."Scan/".$y."/web/webtc/indexcaller.php".'?key='.$inputword.'&input=slp1&output=SktDevaUnicode" target="_blank">'.$ref."</a>"; 
}
function weblink1($dict,$inputword)
{
	$y=Cologne_hrefyear($dict);
	return '<a href="'."http://www.sanskrit-lexicon.uni-koeln.de/scans/".$dict."Scan/".$y."/web/webtc/indexcaller.php".'?key='.$inputword.'&input=slp1&output=SktDevaUnicode" target="_blank">'.$inputword."</a>"; 
}
function Cologne_hrefyear($dict) {
// This could be written using an associative array
$dictionaryname=array("ACC","CAE","AE","AP90","AP","BEN","BHS","BOP","BOR","BUR","CCS","GRA","GST","IEG","INM","KRM","MCI","MD","MW72","MW","MWE","PD","PE","PGN","PUI","PWG","PW","SCH","SHS","SKD","SNP","STC","VCP","VEI","WIL","YAT");
$hrefyear = array("2014","2014","2014","2014","2014","2014","2014","2014","2014","2013","2014","2014","2014","2014","2013","2014","2014","2014","2014","2014","2013","2014","2014","2014","2014","2013","2014","2014","2014","2013","2014","2013","2013","2014","2014","2014");
 $ans = '?';
 for($i=0;$i<count($dictionaryname);$i++) {
  if ($dict == $dictionaryname[$i]){
   $ans = $hrefyear[$i];
   break;
  }
 }
 return $ans;
}

?>