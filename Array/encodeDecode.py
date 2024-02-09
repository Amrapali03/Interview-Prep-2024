
class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        """
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
       
        result = []
        i = 0
        # each interation reads one word of structure(4#neet5#co#de)
        while i < len(s): # read each string
        # new pointer
            j= i
            while s[j] != "#": # till we see int char
                j += 1 # keep incrementing
                # not including j as it is #, we get the integer
                # length gives how many following chars we need to read after j, it is str so change to int
            length = int(s[i:j])
            # j is #, start from there and go till end of str
            read_all_after_int = s[j + 1: j+1 + length]
            result.append(read_all_after_int)
            # iterate i
            i = j +1 + length
        return result


# Your Codec object will be instantiated and called as such:

def main():
    codec = Codec()
    print(codec.decode(codec.encode(["Hello","World"])))

if __name__ == '__main__':
    main()