module Util

using Printf

getpath(path) = joinpath(@__DIR__, "../input/$path")

function getinput(path)
	return readlines(getpath(path))
end

function getinputn(path)
	return read(getpath(path), String)
end

end
