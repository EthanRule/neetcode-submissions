class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image
        image[sr][sc] = color

        # up
        if sr - 1 >= 0 and image[sr - 1][sc] == original_color:
            image = self.floodFill(image, sr - 1, sc, color)
        if sr + 1 < len(image) and image[sr + 1][sc] == original_color:
            image = self.floodFill(image, sr + 1, sc, color)
        if sc - 1 >= 0 and image[sr][sc - 1] == original_color:
            image = self.floodFill(image, sr, sc - 1, color)
        if sc + 1 < len(image[0]) and image[sr][sc + 1] == original_color:
            print("going right")
            image = self.floodFill(image, sr, sc + 1, color)

        return image
        # 2 2 2
        # 2 2 0
        # 2 0 2

        # 1 1 1
        # 1 1 0
        # 1 0 1