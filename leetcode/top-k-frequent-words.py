class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = Counter(words)
        freq = sorted(freq, key = lambda w: (-freq[w],w))
        ret = []
        for i in range(k):
            if(i >= len(freq)):
                break
            ret.append(freq[i])
        return ret