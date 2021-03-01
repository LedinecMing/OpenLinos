function print(string,ended)
	if(type (string)==type (''))
	then
		io.write(string)
	end
	if(type(string)==type({}))
	then
		for i=1,#string
		do 
			io.write(string[i])
		end
	end
	if(ended)
	then 
		io.write('\n')
	end
end
