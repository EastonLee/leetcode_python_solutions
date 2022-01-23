import bisect
import collections
import cProfile
import heapq
import itertools
import math
import re
import unittest
from pprint import pprint

import numpy as np

'''

'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def tree_deserialize(string):
    """
    author: @StefanPochmann
    """
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def tree_height(root):
    """
    author: @StefanPochmann
    """
    return 1 + max(tree_height(root.left), tree_height(root.right)) if root else -1


def tree_draw(root):
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)
    import turtle
    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = tree_height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


class Solution(object):

    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = set(words)
        def can_be_remove(w, l):
            for li in l:
                if li.endswith(w):
                    return True
            return False
        words = sorted(words, key=len)
        N = len(words)
        idx = {}
        seen = set()
        pre = 0
        for i, w in enumerate( words):
            if len(w) not in idx and i > 0 and len(w) not in seen:
                idx[len(words[pre])] = i
            seen.add(len(words[i]))
            pre = i
        idx[len(words[-1])] = N
        rst = 0
        for i in range(N):
            tmp = len(words[i])
            if not can_be_remove(words[i], words[idx[tmp]:]):
                rst += len(words[i]) + 1

        return rst


class Test(unittest.TestCase):

    def test(self):
        cases = [
            #[["time", "me", "bell"], 10],
            [["eeoosum","haxftt","uaimilp","nbtvp","lkgoet","jqpeq","efcrx","aunrxzf","ucderw","egnvf","fgcgu","lqpxcgn","zhejjw","xqkut","gphsi","vmdljk","eblyc","ovccia","tusqhgq","yosub","feuldl","xhqvioc","kmqxdi","ruesqy","nnjnonl","winksex","jixhp","jtwmih","cfngje","zqbiuvf","kwchrda","jfcmw","qjtmpxq","plfhwe","bkrgtp","prtoqyf","icscb","vnnqmfl","raxivhv","unuuwa","noctv","qzdgbi","oxdlj","adpbpor","qahgwwt","ovexlgi","cryoepk","hjwllol","ugjkjz","uknne","qwsebx","brgkrha","fmgaj","ljqap","iufsjg","zybush","schzd","lfufh","bmsay","mpmocyn","zuayq","hwwpo","bzpdj","kiuuzdm","iavrhiu","yyrgn","mrzdw","rdmvhvi","zjnrwsh","ilnql","islnds","vtrejg","mlxarh","zojwiz","xrekc","wkqkuba","xhugc","vvhduu","qdhzxv","iqsmjui","vqlod","yhffx","yrsrak","lhsawd","xndkip","cfjpj","bqncoui","zvfnm","uwllt","pzcnep","awjln","ibdgq","dybxekk","lxzqhzf","idezsoh","ppfmr","hmfstvc","nxuaxt","wllbl","efptaq","xwcpmr","jcylv","cbyefr","hbkicfl","hfvrc","sgxtv","yffcd","frswkd","jnfnb","avpgmh","oozut","kxaqzi","fmvjjll","ipsee","qhtwlse","vadfitk","lwelj","pglpez","voatmoj","jtbkj","nbdvj","izihuu","yyequi","hjzhj","luncrx","qtdbnww","zxfhdag","yqaari","ntzohfk","viwttw","ebtup","kbfqht","zvyuq","lgdnida","eipafux","tdpah","rgnjwrg","dddmjd","xizxkg","xwhtloc","fevqzk","ieazlnp","oyqzskn","thhfuz","cpskz","ersojl","xcsogk","jtaqtu","vhuou","gwrpdmt","uqlcn","gsdvod","vvjqet","txslv","ihctmq","wdwswsg","vtcyil","jtusn","chpbyi","wyqpeou","fcxaam","ijkaxu","airju","qrnwm","vgqnw","jlngn","nqphimk","rvgyu","pzbncj","mtswa","vhkmouy","ocyqzkz","pvoqb","hceqxd","pannkvc","yycue","suzro","eqjnk","obwvj","nptdsic","dqlojte","shddwfp","gzchrbp","cjgve","iygusdl","rypzw","jimbxxf","zisyuil","iqzcfo","rvezja","mapxmae","sblqdp","achdkz","bwyfd","bxhts","klpll","baykcto","vtcgqk","osjsxl","myhaspg","mzyorm","izgcoli","auimay","wgclop","heypfn","jvksmpz","mzbjlsl","sqfvjz","liowk","ioptok","xbcyzz","qkaigo","txeypk","muykti","vxzylqb","txzwf","njzaq","vmyyxvu","wmzku","njuekjj","etyue","cexwit","okvfq","pknesw","vmuizqn","adldh","clqcxkp","ixcxb","dskgxab","lfpgd","umbubg","bebeam","lwwdx","sdmio","jkqcyiz","gjqwcjv","vgthb","ogasxkm","xauldz","uednj","mcncrbx","ebklgfc","wpafz","twqiyxr","lblub","nehqqly","bltvoj","jyzbq","csjuiq","qelalp","qlwqeq","zvjuwub","bxniqgp","aysck","yxyfad","zdqvf","tortm","bthaf","plzzcir","wqihxcb","deivfqb","evfxcuh","lwuvuqo","haohvob","bmqmlwx","tzetn","wglopko","btmlag","fovzkxx","rcset","iigrhgu","ohmxaon","tyzzgcz","oiwiywx","rdlnte","brdlur","jqfxlc","ohiatn","zmbima","okgcr","ftrjz","ufika","xrogzlk","fkezvic","xsyzztf","slskrh","dsisws","pntcusz","erittp","sdcygmg","dhivzg","fvoepjc","ehwdmp","ytldcpl","ftredc","xpgot","eieshe","tllvjy","hweln","wvqgntg","mpgnu","rswckfu","vflgas","etcpjx","ysgre","tmfmcx","sobkyvd","npogznl","ljyaz","bqyxel","xzgwxo","lwqflz","dqqhtjo","zqtvaiw","xqgnlv","ddmnc","wazxy","bewzz","zpjhrr","rybtcsk","xacisyd","yimnfbl","jadevl","wqgzhvx","uulles","rodzypz","fitietn","iqekq","saakv","ncjufr","yyqit","poxqfg","ycnnmt","dzwfqpb","xxlrhs","hoffsj","vbxccdp","ossfnm","ijhlz","qwqpkm","wkvelrl","kovxrec","vwuwp","sehia","gtbxh","tzqlhrc","eqhlwi","egjyj","aklzn","pakzg","jxcnn","iehuw","cvcekz","gczokd","suqlfg","ctadzzj","ccpnz","jtimd","jtjdolt","xezlw","zkaefj","hiboqr","atddqw","lvgztt","gglhju","uesnc","clgnb","ddgba","zngjd","vnvea","mqggxe","iiweifk","hdmaqbb","odqefmu","hvoxfy","foefyv","nkwcdgm","kbnwvo","pugdfzw","ovfjcee","lsdazsh","gcwrdh","ivlkgip","bgtza","liqni","nsxse","qhbeup","exbphm","jfumn","ismhize","spsmmim","yfnht","whwnwpt","gnaoe","tigwk","inptwr","xqvieyv","aocunlg","oultfgk","cxctrl","qmapn","zzvheo","opwowh","cphuphh","mjpafx","zydvhh","txnrvll","zjgvukg","lgsgy","aegnwl","mulblb","kfyam","niisi","ajkfxk","fpcaysm","kocdn","ujjsiwd","ordnli","zojan","jpqbgjp","vjonpp","yakde","zayowe","rssfco","dqverz","amthpad","jxjag","hsqfvg","qwgpwfz","jcdold","wlnvjuo","gvlbas","hflsld","htemb","uiirkvq","bcgvy","woxci","ogtnzp","lswqge","fouzmp","rvrme","ldhrtk","aymayj","ntcptc","isafcpm","njnyicx","htpnq","mjtmnqx","cqyvivg","zvpctzz","sijod","czshr","dobzcc","vccyg","ckimkd","yvxsskm","kqgbb","mwsgr","lhuynx","kxjci","dwujamr","mjrimch","yapaze","fdicle","vlrotdy","nxide","qaiix","zeltf","rhsqvsu","woovi","mgtrsli","szsng","omudfyg","trfyzjj","yzbwkfr","xcubgjy","frxvk","cwbxns","ecgxhjq","ntjws","worbi","ppylwdx","llzqjkw","luwxslb","lurgoz","vkzap","nakrv","ianwx","ryyrk","kxjrei","hlzuc","hvqhv","chsaq","jutzyx","pqzlqgc","oygsl","ifpfpx","xqfiy","zrzghkp","bttgsq","pvovhip","cezsrny","dzrfjcu","mqyzffl","rkpby","xbbaesz","infnegs","dccljk","mbvam","pzbjoy","tbvbp","fxkatg","sykle","hsvxvf","xkapfzl","ojjkwvj","calcmod","zpcpn","pqccrta","wgvkeo","vaglnss","vhbpnv","haallqr","zbqlkux","vmhngff","nhdsnjb","wkdyfy","escesw","odpuns","twarb","ridxfb","lobdggt","tsuqek","mvfzk","ytzvy","mbzuzx","ikjxnrf","gqywj","ytkbm","oipzlc","edtotfb","aabeewo","alzld","cwpgl","dcaefj","gkufvnl","tyihyh","yuwxz","rwdlw","pgjzy","dealp","yklygsb","torbzay","sglfvy","qatvjgi","fjpgm","pqdhgz","snuic","rvgdghm","yshlma","wjpsmm","qrlvyxc","sczhui","fszybb","quacw","jmrsn","rvqsueq","czsyqzn","nlopo","aakfu","mjzdgn","vlvvm","hloms","dierr","lmdcttq","yvzfwr","mdgvacz","wcekt","ttaagl","zjgfhon","dwubhjv","tqydzm","duohsy","ujfiu","dkkmcnx","yuhwuy","vmqaxe","ifkdllq","zlfew","apwics","ytkey","bppax","uriymi","dhgqoua","xxiig","zfogpr","beuxr","xcfjf","dywil","tefepn","rsufgo","buryx","tznxzs","ekank","jdfbnag","cfrrb","rrzvd","ivgcopl","ypqnl","tjeksdi","tbcqx","qkiymjd","ynqjog","mtiagj","ibszkbf","uykabep","mbeonm","clzqgx","mxnism","aymjisb","nyewqd","bcxngax","fpydtc","puvdy","ylnaihr","rauoent","tvtjnjs","gmmrz","adcmrvp","jpzdtuh","kywafq","sjqmfn","jznfx","zejcmbt","ggbajqf","llzrqk","omzmdga","oxanmui","qlbwqc","gefdft","shrxrxv","ctlmi","irztl","uwjckby","otcvkc","grrnzow","gschs","mbkjzk","dnowe","vcatqza","tjohq","haqon","pdxnbxb","rxrumik","qljmc","ellqs","xzdpb","cbjdoot","ayzws","lbjmmtf","yfsblv","kikhaq","ifhzksf","xygsm","ojtmwi","favsi","ofvrf","jknzmu","zeslx","pmyqhew","zswvg","meczedp","zegdend","rraiqlu","rvwemb","lfjfdcs","qlgfcv","fkvbx","ervjzq","ajkgmc","qjbng","xwwipk","fzuhz","bokre","sbrodj","bmkvr","vshwzab","tzweyzk","exnhyuw","jrefvzg","iwbca","ketfce","yalqe","cooev","fehywbq","nbsijw","mlryoxe","ujxmdi","sychszk","thgzkv","vqytlu","osywe","nqqhpk","conksky","emkzv","hmckhn","lgcwvs","sasase","bhekwxn","hrkanv","ejewrw","dwwbnsp","cgejadm","sxyin","acklsb","htqrkj","jeqmzsj","ekgoni","tuuoxz","pmjilbs","zvweq","wslberf","zkvatb","nkfdhk","ujzjj","xrpmlu","kebyfos","jbwfakj","dxgta","sneksk","ikhuqrk","mfcqbz","wuvgqg","ysrno","azoerlj","hnltfl","smwwwx","tiotp","ldupe","telvmq","alzfrq","bdjitts","xitou","jvfluf","cwyha","zcqmvaz","ipwtpms","rtbghe","hohrsx","fctuszf","rqmnwc","vzwhuey","siaybf","wbnrr","udpxmyx","tquqhtm","gxkzgc","wovbk","rkufj","judvce","lupsp","jsaosg","nrmop","ircuihz","azplg","bncnxfe","hyqiya","depon","vfcst","wsllaey","wtenkih","wsziya","vrxtk","xgggdo","bqbntlm","qclurd","hljtrv","lmigsfb","dwsadzg","xdwiiuz","pmsir","wblknh","lmpcjbx","gyfle","zhazje","pvplpi","yonwo","jwssu","erhgovr","mlesr","wgoix","kssbvl","qqliffw","cxlzm","gxhgup","tzkaog","khcadel","pvjanj","jdcax","jfcpoc","uylgu","yvkmb","lwaju","glily","wbdbmt","wuslsmj","kgpppxe","jabcu","amwpefs","lvjwmzk","msosx","xcvxaqe","hvegvrj","hdfbvet","qemdcb","zfbvlsx","imkpx","lypsl","xpenoia","uvzyeg","esguzex","yosvmm","elnncv","obdlsia","paobfh","damgod","remngk","rxdcr","fqgwvs","fgcyq","tsdfdvk","stmlvh","rwoccn","thaqq","niyfnmg","lkwvjme","vkgdpc","tawgg","fpyeqtv","mmtqcaa","sjheq","zeysgv","ahuqvr","jawkstv","nrngh","pvxvre","grgmik","amuqwli","bdfsihi","yuhtj","qcvkzp","jodvci","qdawgu","ffncfp","znhtgms","xopua","nnjqa","anpqxfy","xtveov","prqvsp","cijpgrt","qpdtl","ontgxb","hwvdut","oykxcz","snplsyc","ljjfn","ljtcg","vudptfs","bqjfbq","gkmqfnq","ljpevxy","qgpydh","fgmhnya","vfmiqg","zxudp","oznhw","euqjd","hiafa","vunoif","yrkanq","sjznzuy","piozmgw","mgqim","matcym","ezxmn","chafpk","bprqecx","coxplcf","lbsuwtk","nrlegr","wwwzw","udiaz","rzaypz","kpwvrw","rrqxn","iekkxiu","gaoifkg","yhrqp","rljeo","qnkatee","slrorw","ypzjcc","jzdwqa","mcathrk","tqvln","edcnb","cvoxpqv","bbswh","zekessm","nlwnppy","vnbhptx","mtoii","rakhdl","jbrzpre","jlfmjyz","fihgh","ylszkxe","fvsmi","ltbbnlr","wlbzah","tjfogj","hwuyza","motlkbq","efgyorx","czdip","qljhvw","glybkj","muswalu","tkgcvok","lfngdi","dspxvz","bwzepom","nnthik","uexonsy","owjdrtl","tkgjy","upkghe","imaktpc","jrbrnp","unvcopj","sjppqz","opuuyjw","bmfshz","suvufsh","hdgcsxb","fnvir","gzxefn","lagbahw","tcmthfa","tfqpvol","swgnb","vaesdw","stctoz","wlejm","rohdd","wprty","lgabi","lkpssge","lgdgg","tdzlmge","itzthfl","iirbtv","rtayo","bfugbz","ehprvr","jczoo","zlojiku","hliqsu","uhpcgo","jiklh","hgihi","ugszao","pzigqs","vcaog","fyuvgrk","jigov","vvlly","cluduel","tcthss","mvwsbce","tttdgry","hmuuen","hpatiew","kfknshp","jjdsi","zgzka","mwhmmk","mxikcli","ufnra","aancgn","ocmdkww","tmlouzw","vffksgt","fhvsqs","yenozc","vbktthu","rwhqfj","cukkhe","wujjzzj","idliee","hmtbee","aixnj","ldcny","pnykhz","lyurqx","lrxlsu","aitjmf","xlmkr","rguyze","xeqlzbq","crtnrp","rvtpag","xpksi","ylrzz","xzxzf","bpwreva","zstgyj","amjev","vstzkr","tsvfk","mbnpu","berjf","yweaqx","wwcbedm","gubvbt","rfalub","nzwuf","vyesyg","hzxiai","rqytdr","vzuws","ouqjgx","naffjlc","stunpl","sqlvhob","pkqin","losuhu","blqiv","tlsakt","hqzbi","otkxhk","ssfeal","qlwcb","ngeusq","ynbidv","mfcsivz","dikyim","lrwsdj","nrudz","bcdgo","vzijm","dfayeqt","vhsraqp","buyik","ggsyf","temfwa","xlxmica","nypmhxf","qedzo","apymdqo","gkzva","tqkoev","tvfvdiz","cpfkro","medjvw","umhalo","yiefrmq","tmubr","hbjjxm","qulhnu","myjrhim","moozq","bhljta","fxiknt","ldveki","oeqgbk","ahdaizz","cvwix","wwdsa","ecicir","bvgpf","pmevb","edhwjz","qotvyf","canpt","odqej","zotfkje","wlhpd","jnqnq","fedob","gltfet","yzkwv","xjrkyfp","eshsows","kznspd","oxtbbh","uydxm","eihmiij","zddul","vbfcnwr","jwhcg","rcjce","xveywh","pzhxh","wfejog","mrzph","qkwdae","anhpv","fzpapac","ltjyo","bbfzyna","zpvzbbu","myuvhe","axgin","qkdgap","nzmlrcp","kursnvs","vyutla","izjygk","ibjrsg","vdedqrg","dyvwvnx","rwuukj","jlyod","idwro","soxdp","wbsuth","toiqrf","pkjpa","wayfz","kjlslch","fwvzc","pkhxtuh","sbkjkl","yfdmx","kuljpu","mvqubi","ipteomd","diuoy","qpffr","mnsnix","llzvrri","pkjoaxi","aiqex","sxdkx","xajqw","scdqeui","zgwomgi","yjmrzez","vmznm","zdnft","xegzt","chpykgt","kvrxj","miwvfoz","oypknv","nqmoi","knpisvr","mflfaix","tocde","qftsodc","anoox","whdjwss","zipojy","veaatpt","awedar","aybon","csumks","bwseh","pzttntn","bzrdxp","rejwjxt","boozr","ssrqqo","uyoit","hofzvi","aaertz","eprjebc","hddsxc","hcfsv","bftdo","kyivw","vnomwsb","mjvcd","eqdlvo","eennkhs","jadogre","pdxejko","eghqq","fnbkek","kihtwqg","kipubhp","skvrkz","kwesr","pjnfocg","fiogzqb","iznbs","uzrbwcn","znvmk","kvhpvv","dzwvgh","wptmzc","xpafsqt","wppnzdd","ypzuwrk","kqbcrg","ykrmwsw","qvahwzy","lpahqbt","ffwyrck","zabosn","stogy","qxeppy","cdmykg","vhqsgzp","gozxk","zfxhn","slxufx","zvouro","flnafq","hzpqt","wkrhxd","qbdmrl","rbpkplc","kzrujfk","xlhcp","pcaes","bicnpzg","hgjqivy","japux","sutvoy","oepbgep","baeayiu","taqlsl","wpoiq","bdryqn","vrtukl","ifptkpr","swowet","jffqv","lbgnj","iqdcnrw","yzzova","jolowg","obwuqw","lfjgyhm","qvjykw","ficlspa","iigfkzi","pywwrd","yugpap","lqqee","fpzxfea","lawrll","uedldua","mhawj","llpet","vsdhmcv","oqbvg","xmqwd","ehhhmy","oqisyq","ldzke","fxrfbkv","kufgvcx","cwlts","tdzyir","ibruh","eficnhh","ehhkqhb","kybld","qnwyge","rfwevzy","mkpyfv","svvrb","ubzbu","vlnto","bwucfhq","abmqm","ubdyz","eunkpip","descxdi","ttbvigy","apenhlv","nlwbqoo","invazb","angjca","wdodfqb","pjhwl","nsnibw","klhngp","efesrt","iroqfm","mfpljs","qiikzrp","imfja","buiij","axlye","ywizhv","jgesl","rteqvcj","srblwn","gjsmmn","xudofz","hzslf","iwrtlrj","frsgeb","wwxbrf","tltlle","aihth","luuvh","ardif","pkzboza","jgxej","iyvdo","dittcsq","mbges","ikakqvw","pwihxw","jxlcp","dklac","nyyxa","siusaa","hqtzvct","ljodgn","yujegt","pqhue","hamoan","xyemsce","aounya","zbiibnh","ebadqlj","loeyrj","clljj","vrbda","eedrc","mvkkolh","zxtjrof","hakbgu","ejjqqsb","ikybyik","zgnlg","ajtey","klpfx","mfwpznr","hfycqy","rbvco","lcujpk","apjdc","vlizksw","mhlywcc","yhtox","phefm","bpdrx","acdahic","anclbp","xkwrbhn","jffmvb","qpmny","qexhicw","vawjgdg","kuxbjr","ogkysr","dndevm","feitlq","iqcicu","hcocrcr","opfrcqs","drcbz","cigayx","gtkusr","qwpidpf","kpkpc","pqrde","yoelm","buvalh","oorji","atzrnn","mrwpb","tuvajse","nxhwbt","yvjhlia","xhkfcb","jrhma","fkslmff","sxaad","fwbil","ghqdbqx","slvlrhv","aordc","qaxkzw","pdnxebq","bulnmq","aupyn","twgzpq","wgaqja","oerpb","qtmvf","hgzsgcn","qiyabsv","ukkze","flyrlp","rrjvn","lpiwnjg","xzsjme","omoshhu","iptsvu","zuuka","txfbvt","atbmmj","oxdhgqw","zxamqxx","wwhhhyf","jmnnl","uzcfoge","fbydvn","qdioz","lwcsgaz","fdtcyob","pgmwh","sbelv","chhrtyd","zpfsoo","kymyzy","wuuhg","qakxr","qbowte","yxmexmp","wzdsrki","sukaq","lukthw","yylxc","lbygq","hugpi","sbglvk","kvuwenj","efskwj","zqhepb","cbrrx","uosgmp","dgslz","eiglx","mebqvrj","nvgrjq","zvgzy","hspmk","yjwgc","epvev","rdvgdk","ceotysz","owngjcy","zctes","jzzent","erhxkf","jshewll","aqibg","fhclel","akflepc","dtkckc","rtwrz","aavohm","bncjgw","sdvlpz","bzfop","eqxok","lpraq","mhmxop","oogknp","rmpfl","gkhzqi","pnrzv","orwjtxv","hhnplec","gdvlwtj","pwcaptv","frcoas","hmknh","pngrsu","wxnnxr","xrpjvr","qbsqpw","nghniz","rguowvi","gyqptqe","bnvsg","vdumj","jedcvl","aensd","hvnsie","nwghd","kvnmxu","ccixr","nvdbfje","odrzdun","pgmdrx","mdyyw","yvfdcx","uovmgr","byigmk","ygmes","olpgpcx","myuju","vnpgdz","khaeto","mqqzru","favxch","gabbqgj","wikzwy","bqmfolb","djljj","efiapqn","rmecqh","pjszg","pkxea","vnenh","fvpjjhi","dfemvfs","rxptgi","xenvclw","rvypvq","cmqhs","sxctwyt","vwrpz","tynot","vfahf","rdjopc","noosm","vufuew","iktjih","dijcr","qjptzyv","hhlnkz","mvlvvef","mjfkieq","mzbvxc","iucvv","iqjthb","jttqtkd","bwkhdep","wgfrj","pbhmzf","qnoys","soigaep","zleozzx","bekud","hxkxks","dvgbrzd","xknnd","lhkbxd","rvwwo","yulfn","xodlumx","whgia","ztuwkkl","tljeig","vhjjwn","qjtbflt","melguk","maalqz","fqzfk","ozigp","ccsot","hwkxi","prkeo","tebrc","jzbmyxt","ltcpx","mmxld","xxfeern","tzwgnv","qskkm","sbdme","lhzlv","whmnuwp","wvidtf","ujxtwbb","xdwdfp","rzdnrdq","pozkg","oqsgc","azskfw","ukwgrau","hcmuntk","ilppfip","fkfiv","gyaqm","eimlp","msail","ptsnx","vegiwv","rsbhdg","meluc","srzvmg","tseny","hpjur","kwiaf","owyzp","gdrwi","jgnmmgn","ykfeep","eynnpye","hezcc","lxiqy","hhvfe","bnyyupy","oooyi","cmcfye","wliahtd","pmnzq","klkgw","xcponi","xtjvnz","lwtrzwa","obdmxw","jqxok","udwwb","nlgxjen","eselxvm","eefpg","qonzun","cazyto","fncvzgs","uydlam","idcqmyv","osmjiyb","ordbz","gmvasn","lmjpwxa","skubv","juggzh","duyms","lnzgar","mymyj","vkfvx","poamqwd","qthwwr","ryjru","pzxldd","gajsldd","drsstne","wekyohk","bdnqkc","knmqa","quyidm","sgvkjpg","dlhqny","xudxhy","yjcix","drxef","pbyakr","djcjxh","brvvfm","hkqbj","xsnyj","fvjiq","yocwg","hefjy","tesfb","qjbncvy","jqgwlbj","fgvxmr","xyuxr","adafzb","vulysyb","zzdgwn","erburpz","dxxej","qhguek","goijsy","lccqhe","yplav","zssby","zzxhy","vmpojk","gdaeon","gfibjfm","rpyzxv","pusyrh","ytgfdi","opxuruo","ipxwtkn","qspht","troys","jajvewj","wslekx","aviahr","aqwln","nyrqfn","bzvuvn","fenqqg","ktyefab","ntlvrns","zvadgm","xsyatr","lmtyrka","dzbmjxr","sodgerp","xnagas","xfddyia","yswwrsk","pvlblc","gdqepn","tlduupg","uelup","bszlme","qfgbn","uyqyrt","jochbig","vilhdx","xlluv","gkgxln","rdzvak","mrnnny","jfgzjv","xbvwfyu","xgybs","cheen","bbvpy","ojqreo","qnfuhj","znboy","wnoek","ezgnur","ocrbenn","wkfux","kdkfcs","aggofd","kuvrc","gbpwk","klcujdq","uicaus","mzhjfx","goyxeo","zmfsmfc","vkosier","xgmbse","awcunkn","lsslau","syqdv","fsponoz","bafaw","nsyts","mxjzkzh","fnyjjf","pzarrdv","szsjcn","yoply","zibtoh","tjofv","adhpxmx","ecoeufi","ggoavi","ihzgn","hkfreeh","thvaj","mpwyna","aygzu","blnutp","gknqgep","shweq","drxkoru","imrkvbm","eptrma","vbshxc","pzmiw","owfbc","xmnof","rcunr","qesakpd","tdabt","ikonxb","hmpyhui","vdwduw","kmvfmb","vayin","uhflq","zuaooo","jryivlk","frmdu","jqcvsed","pykujz","ltgmwn","thfgbzj","kummlv","ocwpmz","bkcxby","sjifus","fpjfhz","mdbeopq","fgkja","arjoywd","eehfrmt","bpjkl","kjkkd","ubqtyk","rjnisrj","plycknq","rhlpgwz","ndueo","dxtfqbu","edechwi","sinjq","vxctw","iwezvx","rlzgr","agpxeew","lapcsrd","ikxzuhg","uasmu","xopjfs","xaaxsri","amaww","vwceeh","ownzqw","hfxrfh","dvosdv","zfixlhs","drjrkmq","iggtszi","npjtqwi","cazyuts","cirpbfi","hdmkij","ksfjb","qbskx","sbleci","zusyoz","jddarzn","txavnh","scboq","libvx","hgpggik","dhkbrba","ehvlh","lpzjtyf","obzttku","juxrkf","yptoru","qrhdgea","kmssan","bwkbyfy","elekudj","kqpsnn","dtmrbao","dpkuoj","oemgevh","zjtdwo","asctv","khhkeo","hdutgag","akhwfeb","nohthb","kjdzhyv","gfiadc","bmpyd","sptglh","smwvr","lizej","nyrlw","cyjvf","ubpyfbx","gsiqj","ckygh","neusbl","irhbzoo","wpkvor","vbiexlu","lgdlr","wvhvwc","murjvy","lkifk","txijwg","vegcjvo","ldrtkbr","xdlgzn","kklhui","znoebo","kgvvo","cdmoq","uyyvsv","kgufogv","lprdoy","pvmeygk","ozwjkfj","slbcs","txhmves","ghuyt","oninihs","fltgdkp","xfdux","zonavr","msjyi","judgkpu","yzrll","nsewn","ukwdsxe","yxnowc","rucnuum","iifsl","clwpnbv","cjcyk","skqgk","brbkv","vptbkfl","rntprn","ygjyhlt","qjsxub","gcvkbp","qyrgne","mgxmtf","blgelf","gznlhux","sagaf","aeacxb","bdkkz","ebmxce","vekciy","pzqiq","fohhum","nltebrw","tsgbxay","doeof","mtfjxmo","zmifkat","liswrbf","yiuubyi","ljonb","lombbsl","adwxdqj","whfvq","dylct","kxxki","kiadns","tvtro","qirurr","uqebc","pskzbv","vdidz","gssalzd","oakycj","jfpeuz","gkvwt","unlgu","mvxnt","alfhz","svfwmu","uzwejet","ceyijqs","rcarw","ukxyxbl","eghwq","snfgfa","ghkxs","jxrqtgr","dwobo","stpqzch","hbscnuy","wfsbkc","iyfngnh","usnbds","ictthgo","euvhvco","brppem","rdolxw","wipihv","satjdau","tgvcwz","hcadngj","hjsinq","aofow","staojt","fsktot","jwhxszu","nbpgcsn","rqwmm","viqju","jqfsnad","pmvdi","mygosu","jsseu","moqkh","jdewsps","qhxzb","xzlpzvp","imjdmn","kxfkt","fubrqcr","fzrvf","cvxfyv","lkrjz","xwbfx","aynmll","cellai","jkauqx","tflhoef","wigugbo","hhtoe","xlhwis","zcirs"], 13979]
        ]
        for ci, co in cases:
            assert Solution().minimumLengthEncoding(ci) == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
