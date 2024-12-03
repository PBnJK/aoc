-- Common utilities

function InputLines(path)
	local flines = {}
	for line in io.lines("../input/" .. path) do
		flines[#flines + 1] = line
	end

	return flines
end
