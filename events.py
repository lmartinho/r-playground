import csv

a = {"1":1217,"2":921,"3":541,"4":435,"5":334,"6":265,"7":225,"8":206,"9":177,"10":173,"11":150,"12":119,"13":103,"14":131,"15":108,"16":90,"17":94,"18":94,"19":72,"20":88,"21":74,"22":78,"23":66,"24":63,"25":52,"26":64,"27":46,"28":44,"29":62,"30":46,"31":47,"32":49,"33":33,"34":34,"35":42,"36":39,"37":27,"38":31,"39":28,"40":24,"41":27,"42":20,"43":15,"44":26,"45":26,"46":21,"47":23,"48":23,"49":28,"50":21,"51":13,"52":22,"53":16,"54":14,"55":15,"56":20,"57":22,"58":20,"59":20,"60":16,"61":16,"62":14,"63":16,"64":18,"65":13,"66":13,"67":24,"68":22,"69":10,"70":8,"71":14,"72":6,"73":15,"74":13,"75":10,"76":16,"77":13,"78":12,"79":13,"80":6,"81":9,"82":10,"83":7,"84":10,"85":13,"86":7,"87":8,"88":10,"89":7,"90":9,"91":15,"92":10,"93":6,"94":8,"95":10,"96":9,"97":10,"98":7,"99":14,"100":8,"101":7,"102":4,"103":4,"104":12,"105":11,"106":9,"107":5,"108":9,"109":5,"110":6,"111":8,"112":6,"113":5,"114":3,"115":11,"116":6,"117":3,"118":2,"119":6,"120":6,"121":3,"122":6,"123":2,"124":11,"125":7,"126":5,"127":5,"128":10,"129":9,"130":1,"131":6,"132":4,"133":9,"134":4,"135":7,"136":10,"137":3,"138":6,"139":5,"140":7,"141":5,"142":3,"143":3,"144":4,"145":4,"146":2,"147":4,"148":2,"149":4,"150":6,"151":4,"152":6,"153":3,"154":6,"156":1,"157":3,"158":4,"159":4,"160":1,"161":6,"162":2,"163":3,"164":5,"165":6,"166":3,"167":2,"168":4,"169":4,"170":5,"171":2,"172":1,"173":1,"174":5,"175":5,"176":1,"177":4,"178":2,"179":4,"180":3,"181":4,"182":4,"183":2,"184":2,"185":3,"186":4,"187":5,"188":5,"190":2,"191":3,"192":1,"193":1,"195":2,"196":5,"197":3,"198":1,"199":2,"200":2,"201":2,"202":5,"203":3,"205":1,"206":1,"207":1,"208":1,"209":2,"211":3,"213":2,"214":2,"215":1,"216":2,"217":2,"218":1,"220":2,"221":1,"222":2,"223":3,"224":2,"225":2,"227":1,"228":3,"232":1,"233":3,"234":3,"235":2,"236":2,"237":3,"238":1,"239":3,"240":2,"242":2,"243":4,"244":2,"245":1,"248":5,"249":2,"250":2,"251":2,"252":2,"253":1,"254":1,"255":1,"257":2,"258":3,"260":1,"261":3,"263":3,"265":2,"268":2,"269":1,"272":1,"273":1,"274":1,"275":1,"276":1,"278":1,"281":1,"284":2,"285":1,"286":1,"289":1,"290":1,"291":2,"293":1,"294":1,"295":2,"296":1,"298":1,"299":1,"301":1,"302":1,"305":2,"307":1,"309":3,"310":3,"312":1,"313":1,"315":1,"319":2,"320":3,"321":1,"322":1,"323":2,"327":3,"328":1,"336":5,"337":1,"338":1,"339":1,"343":1,"344":1,"348":1,"351":2,"352":1,"356":3,"359":1,"361":1,"362":1,"364":1,"366":1,"368":1,"369":1,"374":1,"377":1,"378":1,"379":1,"380":2,"381":1,"382":1,"384":1,"385":1,"387":1,"388":2,"389":2,"390":1,"395":1,"402":2,"405":1,"412":2,"420":1,"423":1,"434":1,"436":1,"438":2,"439":1,"452":1,"457":1,"458":1,"460":1,"463":1,"464":2,"476":1,"477":1,"480":1,"481":1,"503":1,"506":1,"513":1,"515":1,"520":1,"528":1,"536":1,"537":1,"538":1,"539":1,"557":1,"562":1,"568":1,"570":1,"571":1,"598":1,"600":1,"601":1,"609":1,"612":1,"615":1,"618":2,"620":1,"637":1,"657":2,"665":1,"681":1,"685":1,"691":1,"700":1,"731":1,"737":1,"739":1,"746":1,"752":1,"763":1,"812":1,"851":1,"858":1,"859":1,"883":1,"892":1,"903":1,"910":1,"912":1,"919":1,"925":1,"931":1,"947":1,"955":1,"959":1,"965":1,"968":1,"1054":1,"1143":1,"1169":1,"1202":1,"1240":1,"1241":1,"1262":1,"1263":1,"1355":1,"1391":1,"1401":1,"1431":1,"1476":1,"1567":1,"1624":1,"1679":1,"1714":1,"1728":1,"1746":1,"1842":1,"1887":1,"1920":1,"2100":1,"2138":1,"2221":1,"2403":1,"2820":1,"3054":1,"3374":1,"3643":1,"3652":1,"3992":1,"4088":1,"4193":1,"4399":1,"4819":1,"5970":1}

with open('events.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['event_count', 'user_count'])
    for k in a:
      spamwriter.writerow([k, a[k]])