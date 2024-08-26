import Control.Monad (forM_)

main :: IO ()
main = do
    putStrLn "Enter a value:"
    input <- getLine
    let n = read input :: Int
    let adjustedN = if n `mod` 2 == 0 then n - 1 else n
    let k = (adjustedN + 1) - 2
    forM_ [1, 3 .. adjustedN] $ \i -> do
        let spaces = replicate (k - (i `div` 2)) ' '
        let stars = replicate i '*'
        putStrLn (spaces ++ stars)
    forM_ [adjustedN - 2, adjustedN - 4 .. 1] $ \i -> do
        let spaces = replicate (k - (i `div` 2)) ' '
        let stars = replicate i '*'
        putStrLn (spaces ++ stars)
