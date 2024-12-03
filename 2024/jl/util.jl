module Util

using Printf

function getinput(path)
	daypath = joinpath(@__DIR__, "../input/$path")
	return readlines(daypath)
end

end
