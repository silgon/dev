function [ isOctave ] = isOctave( )
isOctave = exist('OCTAVE_VERSION') ~= 0;
end

