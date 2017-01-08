# e.g. Given String s = "dir1\n dir11\n dir12\n  picture.jpeg\n  dir121\n  file1.txt\ndir2\n file2.gif";
# So image paths are /dir1/dir12/picture.jpeg and /dir2/file2.gif.
# 1.1 return longest image path to root (return 11, /dir1/dir12)
# 1.2 return longest image path to imgae (return 24, /dir1/dir12/picture.jpeg)
# 1.3 return total image path to root (return 11 + 5 = 16, /dir1/dir12 + /dir2)
# 1.4 return toal image path to image (return 24 + 15 = 39, /dir1/dir12/picture.jpeg + /dir2/file2.gif)

class Solution(object):

    def longestPath(self, input):
    # Map to store the level and the length sum from root to current level.
        maxLength = 0
        pathMap = {0: 0}

        paths = input.strip()
        paths = paths.split("\n")
        imFormat = set(["jpeg", "png", "gif"])

        for path in paths:
            name = path.lstrip()
            # depth is calculated by how many 't' there.
            depth = path.count(" ")
            pathMap[depth + 1] = pathMap[depth] + len(name) + 1
            if "." in name:
                fileName, extension = name.split(".")
                if extension in imFormat:
                    # maxLength = max(maxLength, pathMap[depth])
                    maxLength = max(maxLength, pathMap[depth] + len(name) + 1)

        return maxLength





if __name__ == "__main__":
    obj = Solution()
    n1 = "dir1\n dir11\n dir12\n  picture.jpeg\n  dir121\n  file1.txt\ndir2\n file2.gif"
    n2 = "      dir1\n dir11\n dir12\n  picture.txt\n  dir121\n  file1.txt\ndir2\n file2.gif    "
    n3="dir\n subdir1\n  file1.ext\n  subsubdir1\n subdir2\n  subsubdir2\n   file2.gif"
    print(obj.longestPath(n1))
    print(obj.longestPath(n2))
    print(obj.longestPath(n3))

   