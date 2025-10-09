class Solution:
    def findSubstring(self, s, words):
        wordSize = len(words[0]);
        numWords = len(words);
        
        substringSize = wordSize * numWords;

        answer = [];

        if substringSize > len(s):
            return answer;

        wordCount = dict();

        for i in range(len(words)):
            w = words[i];
            if w in wordCount:
                wordCount[w] += 1;
            else:
                wordCount[w] = 1;

        for i in range(0, len(s) - substringSize + 1):
            tempMap = wordCount.copy();

            j = i;
            count = numWords;

            while j < i + substringSize:
                word = s[j : j + wordSize];

                if word not in tempMap or tempMap[word] == 0:
                    break;

                else:
                    tempMap[word] -= 1;
                    count -= 1;


                j += wordSize
            if count == 0:
                answer.append(i);

        return answer;

        