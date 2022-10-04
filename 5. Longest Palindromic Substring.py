import unittest


class Solution:
    def longestPalindrome2(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        ansL, ansR = 0, 0
        for j in range(len(s)):
            for i in range(j + 1):
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1])
                if dp[i][j]:
                    if j - i > ansR - ansL:
                        ansL, ansR = i, j

        return s[ansL:ansR + 1]

    def longestPalindrome(self, s: str) -> str:
        ansL, ansR = 0, 0
        for i in range(2 * len(s) - 1):
            if i % 2 == 0:
                for j in range(len(s)):
                    if i // 2 - j < 0 or i // 2 + j >= len(s):
                        break
                    if s[i // 2 - j] != s[i // 2 + j]:
                        break
                    if j * 2 > ansR - ansL:
                        ansL, ansR = i // 2 - j, i // 2 + j
            else:
                for j in range(len(s)):
                    if i // 2 - j < 0 or i // 2 + j + 1 >= len(s):
                        break
                    if s[i // 2 - j] != s[i // 2 + j + 1]:
                        break
                    if j * 2 + 1 > ansR - ansL:
                        ansL, ansR = i // 2 - j, i // 2 + j + 1
        return s[ansL:ansR + 1]


class Test(unittest.TestCase):
    def test(self):
        cases = [
            ["babad", "bab"],
            ["cbbd", "bb"],
            [
                "yzwhuvljgkbxonhkpnxldwkaiboqoflbotqamsxyglfqniflcrtsxbsxlwmxowwnnxychyrjedlijejqzsgwakzohghpxgamecmhcalfoyjtutxeciwqupwlxrgdcpfvybskrytvmwkvnbdjitmohjavhmjobudvbsnkvszyrahpanocltwzeubgxkkthxhjgvcvygfkjctkubtjdocncmjzmxujetybdwmqutvrrulhlsbcbripctbkacwoutkrqsohiihiegqqlasykkgjjskgphieofsjlkkmvwcltgjqbpakercxypfcqqsmkowmgjglbzbidapmqoitpzwhupliynjynsdfncaosrfegquetyfhfqohxytqhjxxpskpwxegmnnppnnmgexwpkspxxjhqtyxhoqfhfyteuqgefrsoacnfdsnyjnyilpuhwzptioqmpadibzblgjgmwokmsqqcfpyxcrekapbqjgtlcwvmkkljsfoeihpgksjjgkkysalqqgeihiihosqrktuowcakbtcpirbcbslhlurrvtuqmwdbytejuxmzjmcncodjtbuktcjkfgyvcvgjhxhtkkxgbuezwtlconapharyzsvknsbvdubojmhvajhomtijdbnvkwmvtyrksbyvfpcdgrxlwpuqwicextutjyoflachmcemagxphghozkawgszqjejildejryhcyxnnwwoxmwlxsbxstrclfinqflgyxsmaqtoblfoqobiakwdlxnpkhnoxbkgjlvuhwzy",
                "yzwhuvljgkbxonhkpnxldwkaiboqoflbotqamsxyglfqniflcrtsxbsxlwmxowwnnxychyrjedlijejqzsgwakzohghpxgamecmhcalfoyjtutxeciwqupwlxrgdcpfvybskrytvmwkvnbdjitmohjavhmjobudvbsnkvszyrahpanocltwzeubgxkkthxhjgvcvygfkjctkubtjdocncmjzmxujetybdwmqutvrrulhlsbcbripctbkacwoutkrqsohiihiegqqlasykkgjjskgphieofsjlkkmvwcltgjqbpakercxypfcqqsmkowmgjglbzbidapmqoitpzwhupliynjynsdfncaosrfegquetyfhfqohxytqhjxxpskpwxegmnnppnnmgexwpkspxxjhqtyxhoqfhfyteuqgefrsoacnfdsnyjnyilpuhwzptioqmpadibzblgjgmwokmsqqcfpyxcrekapbqjgtlcwvmkkljsfoeihpgksjjgkkysalqqgeihiihosqrktuowcakbtcpirbcbslhlurrvtuqmwdbytejuxmzjmcncodjtbuktcjkfgyvcvgjhxhtkkxgbuezwtlconapharyzsvknsbvdubojmhvajhomtijdbnvkwmvtyrksbyvfpcdgrxlwpuqwicextutjyoflachmcemagxphghozkawgszqjejildejryhcyxnnwwoxmwlxsbxstrclfinqflgyxsmaqtoblfoqobiakwdlxnpkhnoxbkgjlvuhwzy"],
            [
                "nmxyncuzlwhiobggiowtjexyzbzyhuqmpnyyimazcrnhrnkydxnioqhtchnnoqhuezypyxiepdvyesihlvbuzctptsaowfllxfdqvbwyitsegpbarqqpcrrvemwkglouhhtuxjdeppatdiiwhwvrqxqjcmzhuwurlqrshlsjyxksfjmhykyhcbpmrbsmbrrjwndjsgqdrafidmelnobhtpblozbzttpzheeffwysfrrwtewjnmqoyrvfxmgcmdoadagatwyocixggwppnmtrnfrbiijwojpetuqwknvtqgspuogrbqqptsrljjiaalmqlchlszflyixxpnkttzbrvhzrjzfbpuquuyzwhattxvoqpzieguwvmlrggrlmvwugeizpqovxttahwzyuuqupbfzjrzhvrbzttknpxxiylfzslhclqmlaaijjlrstpqqbrgoupsgqtvnkwqutepjowjiibrfnrtmnppwggxicoywtagadaodmcgmxfvryoqmnjwetwrrfsywffeehzpttzbzolbpthbonlemdifardqgsjdnwjrrbmsbrmpbchykyhmjfskxyjslhsrqlruwuhzmcjqxqrvwhwiidtappedjxuthhuolgkwmevrrcpqqrabpgestiywbvqdfxllfwoastptczubvlhiseyvdpeixypyzeuhqonnhcthqoinxdyknrhnrczamiyynpmquhyzbzyxejtwoiggboihwlzucnyxmn",
                "nmxyncuzlwhiobggiowtjexyzbzyhuqmpnyyimazcrnhrnkydxnioqhtchnnoqhuezypyxiepdvyesihlvbuzctptsaowfllxfdqvbwyitsegpbarqqpcrrvemwkglouhhtuxjdeppatdiiwhwvrqxqjcmzhuwurlqrshlsjyxksfjmhykyhcbpmrbsmbrrjwndjsgqdrafidmelnobhtpblozbzttpzheeffwysfrrwtewjnmqoyrvfxmgcmdoadagatwyocixggwppnmtrnfrbiijwojpetuqwknvtqgspuogrbqqptsrljjiaalmqlchlszflyixxpnkttzbrvhzrjzfbpuquuyzwhattxvoqpzieguwvmlrggrlmvwugeizpqovxttahwzyuuqupbfzjrzhvrbzttknpxxiylfzslhclqmlaaijjlrstpqqbrgoupsgqtvnkwqutepjowjiibrfnrtmnppwggxicoywtagadaodmcgmxfvryoqmnjwetwrrfsywffeehzpttzbzolbpthbonlemdifardqgsjdnwjrrbmsbrmpbchykyhmjfskxyjslhsrqlruwuhzmcjqxqrvwhwiidtappedjxuthhuolgkwmevrrcpqqrabpgestiywbvqdfxllfwoastptczubvlhiseyvdpeixypyzeuhqonnhcthqoinxdyknrhnrczamiyynpmquhyzbzyxejtwoiggboihwlzucnyxmn"]
        ]
        for ci, co in cases:
            result = Solution().longestPalindrome(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
