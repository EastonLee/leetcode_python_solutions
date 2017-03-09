import unittest


class Solution(object):

    # Easton old
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList.append(beginWord)
        if endWord not in wordList: return []
        idx_d = {}
        length = len(beginWord)
        for w in wordList:
            for i in range(length):
                p = w[:i] + '_' + w[i + 1:]
                if p in idx_d:
                    idx_d[p].append(w)
                else:
                    idx_d[p] = [w]
        def get_next(path):
            w = path[-1]
            w = [w[:i] + '_' + w[i + 1:] for i in range(length)]
            rst = {j for i in w for j in idx_d.get(i, []) if j not in path}
            return list(set(rst))

        new = set([beginWord])
        new_memo = [[beginWord]]
        seen = set([beginWord])
        while new:
            new = {j for i in new for j in get_next([i])} - seen
            if endWord in new:
                break
            new_memo.append(list(new))
            seen |= new

        if not new:
            return []
        bt = [[[endWord]]]
        for memo_path in new_memo[::-1]:
            nxt_bt = []
            for i in bt[-1]:
                for j in get_next(i):
                    if j in memo_path:
                        nxt_bt.append(i+[j])
            bt.append(nxt_bt)
        return [i[::-1] for i in bt[-1]]

    # https://discuss.leetcode.com/topic/8343/use-defaultdict-for-traceback-and-easy-writing-20-lines-python-code
    # tusizi 
    def findLadders(self, start, end, dic):
        import string, collections
        dic = set(dic)
        dic.add(end)
        level = {start}
        parents = collections.defaultdict(set)
        while level and end not in parents:
            next_level = collections.defaultdict(set)
            for node in level:
                for char in string.ascii_lowercase:
                    for i in range(len(start)):
                        n = node[:i]+char+node[i+1:]
                        if n in dic and n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level)
        res = [[end]]
        while res and res[0][0] != start:
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res

    # Easton new, fastest
    def findLadders(self, beginWord, endWord, wordList):
        from collections import defaultdict
        pattern_dict = defaultdict(set)
        length = len(beginWord)
        for w in wordList:
            for i in range(length):
                p = w[:i] + '_' + w[i + 1:]
                pattern_dict[p].add(w)
        def get_next(w):
            w_patters = [w[:i] + '_' + w[i + 1:] for i in range(length)]
            return {j for i in w_patters for j in pattern_dict.get(i, []) if i != w}

        pre_level = defaultdict(set, [[beginWord, None]])
        parents = defaultdict(set, [[beginWord, None]])
        while pre_level and endWord not in pre_level:
            cur_level = defaultdict(set)
            for i in pre_level:
                for j in get_next(i):
                    if j not in parents:
                        cur_level[j].add(i)
            pre_level = cur_level
            parents.update(cur_level)
        rst = [[endWord]]
        while rst and rst[0][0] != beginWord:
            rst = [[j] + i for i in rst for j in parents[i[0]] if j not in i]
        return rst

class Test(unittest.TestCase):

    def test(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        rst = [
            ["hit", "hot", "dot", "dog", "cog"],
            ["hit", "hot", "lot", "log", "cog"]
        ]
        assert sorted(Solution().findLadders(beginWord, endWord, wordList)) == sorted(rst)
        beginWord = "cet"
        endWord = "ism"
        wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
        rst = [['cet', 'get', 'gee', 'gte', 'ate', 'ats', 'its', 'ito', 'ibo', 'ibm', 'ism'], ['cet', 'cot', 'con', 'ion', 'inn', 'ins', 'its', 'ito', 'ibo', 'ibm', 'ism'], ['cet', 'cat', 'can', 'ian', 'inn', 'ins', 'its', 'ito', 'ibo', 'ibm', 'ism']]
        assert sorted(Solution().findLadders(beginWord, endWord, wordList)) == sorted(rst)
        beginWord = "a"
        endWord = "c"
        wordList = ["a","b","c"]
        rst = [["a","c"]]
        assert sorted(Solution().findLadders(beginWord, endWord, wordList)) == sorted(rst)
if __name__ == '__main__':
    unittest.main()
