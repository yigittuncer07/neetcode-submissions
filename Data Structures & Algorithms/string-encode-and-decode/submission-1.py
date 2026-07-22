class Solution:

    def encode(self, strs: List[str]) -> str:
        splits = ""
        merged_strings = ""
        for s in strs:
            splits += (str(len(s)) + ",")
            merged_strings += s

        splits += "_"

        return str(splits) + merged_strings      

    def decode(self, s: str) -> List[str]:
        splits, merged_string = s.split('_', 1)
        if not splits:
            return []
        splits = splits[:-1].split(',')
        
        result = []
        for split in splits:
            split = int(split)
            result.append(merged_string[:split])
            merged_string = merged_string[split:]

        return result
