class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0;
        unordered_set<char> chars;
        int length = 0;
        for(int right = 0; right < s.length(); right++)
        {
            while(chars.find(s[right]) != chars.end())
            {
                chars.erase(s[left]);
                left++;
            }
            chars.insert(s[right]);
            if(length < chars.size()) length = chars.size();
        }
        return length;
    }
};
