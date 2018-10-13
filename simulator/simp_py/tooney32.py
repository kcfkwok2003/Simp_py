# This comes with no warranty, implied or otherwise

# This data structure was designed to support Proportional fonts
# on Arduinos. It can however handle any ttf font that has been converted
# using the conversion program. These could be fixed width or proportional 
# fonts. Individual characters do not have to be multiples of 8 bits wide. 
# Any width is fine and does not need to be fixed.

# The data bits are packed to minimize data requirements, but the tradeoff
# is that a header is required per character.

# tooney32.c
# Point Size   : 32
# Memory usage : 5470 bytes
# # characters : 95

# Header Format (to make Arduino UTFT Compatible):
# ------------------------------------------------
# Character Width (Used as a marker to indicate use this format. i.e.: = 0x00)
# Character Height
# First Character (Reserved. 0x00)
# Number Of Characters (Reserved. 0x00)

tft_tooney32 =[
0x00, 0x20, 0x00, 0x00,

# Individual Character Format:
# ----------------------------
# Character Code
# Adjusted Y Offset
# Width
# Height
# xOffset
# xDelta (the distance to move the cursor. Effective width of the character.)
# Data[n]

# NOTE: You can remove any of these characters if they are not needed in
# your application. The first character number in each Glyph indicates
# the ASCII character code. Therefore, these do not have to be sequential.
# Just remove all the content for a particular character to save space.

# ' '
0x20,0x1E,0x00,0x00,0x00,0x09,

# '!'
0x21,0x09,0x0B,0x16,0x00,0x0B,
0x3F,0xC8,0x07,0x81,0x70,0x27,0x00,0xE0,0x1C,0x21,0x84,0x30,0x86,0x10,0xC2,0x18,0x43,0xF0,0x61,0x0C,0x13,0x02,0x60,0x4E,0x09,0xE2,0x1F,0x81,0xE0,0x00,0x00,
# '"'
0x22,0x05,0x0E,0x0A,0xFF,0x0D,
0x04,0x30,0x2D,0x61,0x8C,0x44,0x71,0x31,0x88,0xCE,0x42,0x72,0x18,0xC8,0x7B,0xC0,0xC6,0x00,
# '#'
0x23,0x07,0x18,0x16,0x00,0x18,
0x00,0xFF,0xF8,0x01,0x83,0x08,0x01,0x82,0x08,0x01,0x82,0x08,0x0F,0x06,0x0F,0x10,0x00,0x01,0x30,0x00,0x01,0x30,0x00,0x00,0x20,0x00,0x02,0x7E,0x0C,0x1E,0x7E,0x0C,0x1E,0x60,0x00,0x02,0x60,0x00,0x00,0x40,0x00,0x04,0x40,0x00,0x04,0xC0,0x00,0x04,0xFC,0x10,0x78,0xFC,0x30,0x78,0x08,0x30,0x40,0x18,0x30,0x40,0x1F,0xFF,0x80,0x1F,0xFF,0x80,
# '$'
0x24,0x09,0x0F,0x14,0x00,0x0F,
0x01,0x80,0x04,0xF8,0x18,0x08,0x20,0x10,0xC0,0x41,0x00,0x86,0x01,0x0C,0x12,0x18,0x38,0x30,0x60,0xA0,0x83,0x01,0x06,0x02,0x0C,0x04,0x18,0x10,0x30,0x20,0x6E,0x40,0xFF,0x81,0x9E,0x00,0x18,0x00,
# '%'
0x25,0x07,0x17,0x16,0x00,0x17,
0x0F,0x81,0xF8,0x20,0x84,0x10,0x80,0x98,0x42,0x00,0x21,0x0C,0x01,0x82,0x18,0x43,0x08,0x30,0x04,0x10,0x70,0x18,0x40,0xE0,0x21,0x00,0xF1,0x82,0x00,0xFF,0x0F,0xC0,0xFC,0x10,0x40,0x18,0x40,0x40,0x21,0x80,0x40,0x82,0x00,0x83,0x0C,0x21,0x04,0x18,0x02,0x18,0x78,0x04,0x21,0x30,0x10,0xC2,0x78,0xC3,0xF8,0x7F,0x07,0xE0,0x7C,0x00,
# '&'
0x26,0x08,0x17,0x17,0x00,0x17,
0x01,0xF6,0x00,0x04,0x1A,0x00,0x10,0x04,0x00,0x40,0x10,0x01,0x00,0x40,0x06,0x00,0x80,0x0C,0x1A,0x00,0x18,0x1F,0xC0,0x30,0x18,0xF8,0x60,0x08,0x09,0x80,0x00,0x33,0x00,0x00,0xCC,0x0C,0x01,0x18,0x3C,0x04,0x30,0x30,0x07,0x60,0x00,0x01,0xE0,0x00,0x07,0xC0,0x00,0x09,0xC0,0x0C,0x23,0xC0,0x38,0x03,0xE1,0xF8,0x03,0xFF,0x70,0x01,0xF8,0x60,0x00,
# '''
0x27,0x05,0x09,0x0A,0xFF,0x08,
0x06,0x05,0x86,0x23,0x13,0x11,0x90,0x90,0xC8,0x78,0x18,0x00,
# '('
0x28,0x05,0x0D,0x1D,0x00,0x0D,
0x03,0x00,0x34,0x01,0x90,0x08,0x40,0x81,0x88,0x1C,0xC1,0xC4,0x08,0x60,0x83,0x04,0x10,0x41,0x82,0x0C,0x10,0x60,0x83,0x04,0x18,0x20,0xC0,0x06,0x04,0x38,0x20,0xC0,0x87,0x06,0x38,0x1C,0xE0,0x67,0x86,0x1C,0x60,0x76,0x01,0xE0,0x0E,0x00,0x60,0x00,
# ')'
0x29,0x05,0x0D,0x1D,0x00,0x0D,
0x01,0x00,0x10,0x01,0x20,0x11,0x03,0x04,0x30,0x11,0xE0,0x8F,0x82,0x1C,0x10,0x70,0x81,0x82,0x0E,0x10,0x30,0x81,0x84,0x0C,0x20,0x61,0x02,0x08,0x10,0x01,0x84,0x08,0x20,0x81,0x18,0x11,0x80,0x8E,0x08,0x78,0x80,0xE4,0x03,0xE0,0x0E,0x00,0x30,0x00,
# '*'
0x2A,0x09,0x0C,0x0D,0x01,0x0D,
0x07,0x00,0x88,0x18,0xE4,0x11,0xC0,0x1F,0x8E,0xC0,0x1C,0x11,0xC8,0xBF,0x8E,0x7D,0xC1,0xE0,0x0C,0x00,
# '+'
0x2B,0x09,0x15,0x14,0x00,0x15,
0x00,0x7C,0x00,0x04,0x10,0x00,0x60,0x80,0x07,0x04,0x00,0x38,0x20,0x01,0xC1,0x00,0xFE,0x0F,0xCC,0x00,0x01,0xE0,0x00,0x0F,0x00,0x00,0x78,0x00,0x03,0xFF,0x07,0xFF,0xF8,0x3F,0x7F,0xC1,0xF0,0x0E,0x08,0x00,0x70,0x40,0x03,0x82,0x00,0x1F,0xF0,0x00,0xFE,0x00,0x03,0xE0,0x00,
# ','
0x2C,0x17,0x09,0x0B,0x00,0x09,
0x1E,0x10,0x98,0x38,0x1C,0x0F,0x0B,0xC4,0xE4,0x32,0x1E,0x0E,0x00,
# '-'
0x2D,0x11,0x09,0x06,0x00,0x09,
0x1B,0x90,0x50,0x39,0x2F,0xE7,0xF0,
# '.'
0x2E,0x16,0x09,0x09,0x00,0x09,
0x1E,0x10,0x90,0x38,0x1C,0x0F,0x07,0xCC,0xFC,0x3C,0x00,
# '/'
0x2F,0x09,0x11,0x19,0x00,0x11,
0x00,0x3F,0x80,0x30,0x40,0x30,0x20,0x18,0x20,0x18,0x10,0x0C,0x08,0x06,0x08,0x06,0x04,0x03,0x04,0x03,0x02,0x01,0x81,0x00,0xC1,0x00,0xC0,0x80,0x60,0x00,0x60,0x40,0x30,0x20,0x18,0x20,0x18,0x10,0x0C,0x08,0x06,0x08,0x06,0x04,0x03,0x04,0x03,0xFE,0x01,0xFE,0x00,0xFE,0x00,0x00,
# '0'
0x30,0x08,0x17,0x17,0x00,0x17,
0x00,0x7E,0x00,0x03,0x01,0x80,0x18,0x00,0x80,0x40,0x00,0x81,0x00,0x00,0x86,0x00,0x00,0x08,0x00,0x01,0x30,0x00,0x02,0x40,0x3C,0x03,0x80,0xFC,0x07,0x02,0x3C,0x0E,0x04,0x38,0x1C,0x08,0x30,0x3C,0x08,0x40,0x78,0x0F,0x01,0x30,0x00,0x02,0x70,0x00,0x08,0xF0,0x00,0x10,0xF0,0x00,0xC0,0xF0,0x03,0x00,0xFC,0x1C,0x00,0xFF,0xE0,0x00,0x3F,0x00,0x00,
# '1'
0x31,0x09,0x0D,0x16,0x00,0x0D,
0x00,0x30,0x06,0x40,0xC4,0x18,0x43,0x02,0x20,0x13,0xC0,0x9E,0x04,0x30,0x21,0x81,0x0C,0x08,0x60,0x43,0x02,0x18,0x10,0xC0,0x86,0x04,0x30,0x21,0x81,0x98,0x03,0xFF,0xE7,0xFE,0x00,0x00,
# '2'
0x32,0x08,0x12,0x17,0x00,0x12,
0x00,0xF0,0x00,0x81,0x00,0xC0,0x20,0xE0,0x04,0x40,0x01,0x38,0x00,0x2F,0x84,0x08,0xF9,0x82,0x1F,0xE0,0x81,0xF0,0x00,0x1C,0x10,0x06,0x04,0x01,0x03,0x80,0xC0,0xD0,0x20,0x04,0x18,0x01,0x0C,0x00,0x43,0x00,0x11,0x80,0x04,0x60,0x01,0x3F,0xFF,0x4F,0xFF,0xE0,0x00,0x30,
# '3'
0x33,0x08,0x12,0x17,0x00,0x12,
0x0C,0x00,0x05,0xFF,0xE3,0x00,0x08,0xC0,0x02,0x30,0x01,0x0C,0x00,0x43,0x00,0x10,0xC0,0x0C,0x37,0x01,0x0F,0x80,0x23,0xE0,0x08,0x10,0x01,0x0F,0xE0,0x43,0xF8,0x10,0x4E,0x04,0x23,0x01,0x10,0x00,0x08,0x00,0x24,0x00,0x13,0x00,0x08,0xFC,0x0C,0x1F,0xFE,0x00,0xFE,0x00,
# '4'
0x34,0x09,0x12,0x16,0x00,0x12,
0x00,0x0E,0x00,0x04,0x80,0x06,0x20,0x03,0x08,0x01,0x82,0x00,0xC0,0x80,0x40,0x20,0x20,0x08,0x10,0x03,0x88,0x20,0x94,0x00,0x07,0x00,0x01,0xC0,0x00,0x70,0x00,0x1C,0x00,0x07,0xFE,0x09,0xFF,0x83,0x80,0x60,0xC0,0x30,0x10,0x0F,0xF8,0x03,0xFC,0x00,0x00,0x00,
# '5'
0x35,0x08,0x11,0x17,0x00,0x11,
0x00,0x03,0x00,0xFF,0x40,0x80,0x20,0xC0,0x10,0x60,0x08,0x30,0x04,0x30,0x02,0x18,0x1D,0x0C,0x07,0x06,0x01,0x82,0x00,0x43,0x00,0x11,0xFC,0x08,0xFF,0x04,0x17,0x82,0x18,0x01,0x18,0x00,0x08,0x00,0x8C,0x00,0x8C,0x00,0xC7,0xC1,0xC3,0xFF,0x80,0xBF,0x00,
# '6'
0x36,0x08,0x13,0x17,0x00,0x13,
0x00,0x7F,0xC0,0x30,0x08,0x18,0x01,0x06,0x00,0x41,0x80,0x10,0x60,0x02,0x08,0x0C,0x83,0x00,0x30,0x60,0x01,0x18,0x00,0x13,0x00,0x01,0x60,0x00,0x0C,0x00,0x03,0x80,0xC0,0x78,0x3C,0x0F,0x03,0x01,0x60,0x00,0x0E,0x00,0x08,0xE0,0x02,0x1E,0x00,0x81,0xF0,0x60,0x1F,0xF8,0x00,0xFC,0x00,
# '7'
0x37,0x08,0x12,0x17,0x00,0x12,
0x0C,0x00,0x0D,0xFF,0xF3,0x00,0x04,0xC0,0x02,0x30,0x00,0x8C,0x00,0x43,0x00,0x10,0xDC,0x08,0x3F,0x02,0x0E,0x81,0x00,0x60,0x40,0x10,0x20,0x0C,0x08,0x02,0x04,0x01,0x81,0x00,0x40,0x80,0x30,0x20,0x10,0x10,0x0F,0x04,0x03,0xF1,0x00,0x3F,0x40,0x03,0xE0,0x00,0x30,0x00,
# '8'
0x38,0x08,0x12,0x17,0x00,0x12,
0x01,0xF0,0x00,0x83,0x00,0xC0,0x20,0x20,0x08,0x10,0x01,0x0C,0x18,0x43,0x06,0x10,0xC0,0x04,0x38,0x01,0x0C,0x00,0x42,0x00,0x09,0x80,0x01,0xC0,0x00,0x70,0x3C,0x1C,0x0F,0x07,0x00,0x01,0xE0,0x00,0x9C,0x00,0x27,0x80,0x30,0xF8,0x38,0x1F,0xFC,0x01,0xFC,0x00,0x00,0x00,
# '9'
0x39,0x08,0x13,0x17,0x00,0x13,
0x01,0xF8,0x00,0xC0,0xC0,0x20,0x04,0x08,0x00,0x42,0x00,0x08,0xC0,0x00,0x90,0x18,0x16,0x07,0x81,0xC0,0x60,0x38,0x00,0x07,0x80,0x00,0xF0,0x00,0x17,0x00,0x02,0xF0,0x00,0x0F,0x80,0x10,0xE6,0x02,0x08,0x00,0x83,0x00,0x20,0x40,0x0C,0x10,0x03,0x06,0xC1,0xC0,0xFF,0xE0,0x1F,0xF0,0x00,
# ':'
0x3A,0x0E,0x09,0x11,0x00,0x09,
0x0E,0x10,0x90,0x38,0x1C,0x0F,0x07,0xC4,0xFC,0x3C,0x19,0x98,0x38,0x1C,0x0F,0x07,0xCC,0xFC,0x3C,0x00,
# ';'
0x3B,0x0F,0x09,0x13,0x00,0x09,
0x0E,0x10,0x98,0x38,0x1C,0x0F,0x07,0xC4,0xFC,0x3E,0x19,0x98,0x38,0x1C,0x0F,0x03,0xC4,0xE4,0x32,0x1E,0x0E,0x00,
# '<'
0x3C,0x0A,0x13,0x13,0x00,0x13,
0x00,0x00,0xC0,0x00,0x64,0x00,0x60,0x80,0x30,0x10,0x38,0x02,0x18,0x03,0x8C,0x01,0xE3,0x01,0xF0,0xE0,0xF8,0x1C,0x06,0x03,0x80,0x18,0x7E,0x00,0xCF,0xF0,0x06,0x7F,0xC0,0x43,0xFE,0x08,0x0F,0xF9,0x00,0x7F,0xE0,0x01,0xF8,0x00,0x0C,0x00,
# '='
0x3D,0x0D,0x14,0x0E,0x00,0x14,
0x3F,0xFF,0xE6,0x00,0x01,0xE0,0x00,0x1E,0x00,0x01,0xE0,0x00,0x1F,0xFF,0xFE,0xFF,0xFF,0xE6,0x00,0x01,0x60,0x00,0x1E,0x00,0x01,0xE0,0x00,0x1F,0xFF,0xFE,0xFF,0xFF,0xEF,0xFF,0xF8,
# '>'
0x3E,0x0A,0x13,0x13,0x00,0x13,
0x38,0x00,0x0C,0xC0,0x03,0x87,0x00,0x70,0x18,0x0E,0x00,0xE1,0xF8,0x03,0x3F,0xC0,0x19,0xFF,0x01,0x0F,0xF8,0x20,0x3C,0x04,0x0C,0x00,0x86,0x00,0xE3,0x00,0x78,0xC0,0x7C,0x38,0x3E,0x07,0x3E,0x00,0xFF,0x00,0x1F,0x00,0x03,0x80,0x00,0x00,
# '?'
0x3F,0x08,0x11,0x16,0x00,0x11,
0x00,0xF0,0x01,0x82,0x01,0x00,0x81,0x00,0x23,0x00,0x0B,0x00,0x05,0xC0,0x02,0xF8,0xC1,0x3F,0x40,0x87,0xE0,0x80,0xE0,0x40,0x30,0x40,0x18,0x20,0x0F,0xE0,0x07,0x30,0x03,0x04,0x03,0x02,0x01,0x81,0x00,0xE0,0x80,0x78,0x80,0x1F,0x80,0x07,0x80,
# '@'
0x40,0x09,0x16,0x16,0x00,0x16,
0x00,0x3F,0x00,0x06,0x03,0x00,0x23,0xFB,0x01,0x3F,0xFC,0x09,0x81,0xF8,0x48,0x7F,0xE2,0x44,0x13,0xD9,0x23,0x8F,0x41,0x1E,0x1F,0x2C,0x51,0x7C,0xE0,0xC5,0xF3,0x8B,0x06,0xCE,0x28,0x3B,0x38,0xE2,0xEE,0x71,0x4D,0x19,0xE3,0x88,0x73,0xFF,0xD1,0xE7,0x9F,0xA3,0xC7,0xF1,0x07,0xE0,0x38,0x07,0xFF,0x80,0x07,0xF8,0x00,
# 'A'
0x41,0x08,0x19,0x17,0x00,0x19,
0x00,0x0C,0x00,0x00,0x09,0x00,0x00,0x08,0x80,0x00,0x0C,0x20,0x00,0x04,0x08,0x00,0x06,0x04,0x00,0x02,0x01,0x00,0x03,0x00,0xC0,0x03,0x00,0x20,0x01,0x00,0x08,0x01,0x80,0x04,0x00,0x80,0x01,0x00,0xC0,0xC0,0x40,0xC0,0x60,0x20,0x40,0x00,0x08,0x60,0x00,0x06,0x40,0x00,0x00,0xF0,0x00,0x00,0xFE,0x1F,0xE1,0xCF,0xCF,0xF1,0x81,0xF4,0x1B,0x80,0x3E,0x0F,0x00,0x0E,0x06,0x00,
# 'B'
0x42,0x09,0x13,0x15,0x00,0x13,
0x3F,0xFC,0x0C,0x00,0x61,0xC0,0x06,0x38,0x00,0x43,0x00,0x04,0x60,0x60,0x8C,0x0C,0x11,0x81,0x02,0x30,0x00,0x46,0x00,0x08,0xC0,0x00,0x98,0x18,0x13,0x03,0x02,0x60,0x60,0x4C,0x00,0x09,0x80,0x01,0x30,0x00,0x44,0x00,0x11,0x80,0x0E,0x3F,0xFF,0x07,0xFF,0x80,
# 'C'
0x43,0x08,0x16,0x17,0x00,0x16,
0x00,0x7E,0x00,0x06,0x02,0x00,0x60,0x06,0x02,0x00,0x06,0x10,0x00,0x00,0xC0,0x00,0x22,0x00,0x01,0x18,0x0F,0x18,0x40,0x7E,0xC3,0x02,0x3E,0x0C,0x08,0xF0,0x30,0x21,0x80,0xC0,0x83,0x03,0x81,0x1A,0x0E,0x03,0xC4,0x18,0x00,0x08,0x70,0x00,0x19,0xE0,0x00,0x23,0xC0,0x01,0x87,0x80,0x1E,0x0F,0xC1,0xE0,0x0F,0xFE,0x00,0x0F,0xC0,0x00,
# 'D'
0x44,0x09,0x16,0x15,0xFF,0x15,
0x1F,0xFE,0x00,0x80,0x06,0x07,0x00,0x06,0x1C,0x00,0x0C,0x30,0x00,0x10,0xC0,0x00,0x23,0x00,0x00,0x8C,0x0F,0x01,0x30,0x3E,0x04,0xC0,0xF8,0x13,0x03,0xE0,0x4C,0x0F,0x01,0x30,0x00,0x04,0xC0,0x00,0x23,0x00,0x00,0x8C,0x00,0x04,0x30,0x00,0x20,0x80,0x01,0x06,0x00,0x18,0x1F,0xFF,0x80,0x3F,0xF0,0x00,
# 'E'
0x45,0x08,0x11,0x17,0x00,0x11,
0x00,0x01,0x0F,0xFF,0x48,0x00,0x2C,0x00,0x17,0x00,0x0B,0x80,0x04,0xC0,0x02,0x60,0x01,0x30,0x1A,0x98,0x01,0x8C,0x00,0x86,0x00,0x43,0x00,0x31,0x80,0xD4,0xC0,0x02,0x60,0x01,0x30,0x00,0x98,0x00,0x4C,0x00,0x24,0x00,0x17,0xFF,0xEB,0xFF,0xF8,0x00,0x08,
# 'F'
0x46,0x08,0x11,0x16,0xFF,0x10,
0x00,0x01,0x0F,0xFF,0x48,0x00,0x2E,0x00,0x17,0x00,0x09,0x80,0x04,0xC0,0x02,0x60,0x01,0x30,0x3A,0x98,0x01,0x8C,0x00,0xC6,0x00,0x43,0x00,0x21,0x81,0xD0,0xC0,0xF0,0x60,0x70,0x30,0x20,0x18,0x10,0x08,0x02,0x0C,0x01,0x07,0xFF,0x03,0xFF,0x00,
# 'G'
0x47,0x08,0x16,0x17,0x00,0x16,
0x00,0x7F,0x00,0x06,0x03,0x00,0x60,0x03,0x82,0x00,0x02,0x10,0x00,0x08,0xC0,0x00,0xC2,0x00,0x06,0x18,0x07,0x30,0x40,0x3C,0x83,0x01,0x3C,0x0C,0x04,0xFF,0xB0,0x14,0x02,0xC0,0x78,0x1B,0x80,0xE0,0x4E,0x01,0x81,0x18,0x00,0x04,0x70,0x00,0x11,0xE0,0x00,0x43,0xC0,0x01,0x07,0x80,0x18,0x0F,0x81,0xC0,0x1F,0xFC,0x00,0x0F,0xC0,0x00,
# 'H'
0x48,0x09,0x16,0x15,0x00,0x16,
0x3F,0xC7,0xF9,0x00,0xE0,0x1E,0x03,0xC0,0x98,0x0B,0x02,0x60,0x2C,0x09,0x80,0xF0,0x26,0x00,0x00,0x98,0x00,0x02,0x60,0x00,0x09,0x80,0x00,0x26,0x00,0x00,0x98,0x00,0x02,0x60,0x3C,0x09,0x80,0xF0,0x26,0x02,0xC0,0x98,0x0B,0x02,0x60,0x2C,0x09,0x00,0x20,0x1F,0xFF,0xFF,0xFF,0xF7,0xFC,0x00,0x00,0x00,
# 'I'
0x49,0x09,0x0B,0x15,0x00,0x0B,
0x3F,0xC8,0x07,0x81,0x70,0x26,0x04,0xC0,0x98,0x13,0x02,0x60,0x4C,0x09,0x81,0x30,0x26,0x04,0xC0,0x98,0x13,0x02,0x60,0x48,0x07,0x00,0xFF,0xEF,0xF8,
# 'J'
0x4A,0x09,0x0F,0x16,0x00,0x0F,
0x03,0xFC,0x08,0x04,0x38,0x08,0x70,0x10,0x60,0x20,0xC0,0x41,0x80,0x83,0x01,0x06,0x02,0x0C,0x04,0x18,0x08,0x30,0x10,0xA0,0x23,0x00,0x44,0x00,0x98,0x01,0x20,0x00,0xC0,0x09,0x00,0x27,0xC1,0x8F,0xFE,0x0F,0xF0,0x00,
# 'K'
0x4B,0x08,0x17,0x18,0x00,0x17,
0x00,0x01,0x80,0x7F,0xEE,0x81,0x80,0x38,0x87,0x81,0xE0,0x8F,0x03,0x80,0x86,0x06,0x00,0x8C,0x08,0x07,0x18,0x00,0x1C,0x30,0x00,0x70,0x60,0x01,0x00,0xC0,0x02,0x01,0x80,0x02,0x03,0x00,0x04,0x06,0x04,0x04,0x0C,0x0C,0x04,0x18,0x18,0x06,0x30,0x38,0x00,0x60,0x78,0x09,0x00,0x30,0x26,0x00,0x71,0x8F,0xFF,0xE4,0x0F,0xFC,0xD0,0x00,0x01,0xC0,0x00,0x00,0x00,
# 'L'
0x4C,0x09,0x11,0x16,0x00,0x11,
0x3F,0xF0,0x30,0x04,0x1C,0x06,0x0E,0x02,0x03,0x01,0x01,0x80,0x80,0xC0,0x40,0x60,0x20,0x30,0x10,0x18,0x08,0x0C,0x04,0xC6,0x03,0xD3,0x00,0x09,0x80,0x04,0xC0,0x02,0x60,0x01,0x30,0x00,0xB0,0x00,0x58,0x00,0x2F,0xFF,0xD7,0xFF,0xF0,0x00,0x30,
# 'M'
0x4D,0x09,0x20,0x16,0x00,0x1F,
0x00,0xF8,0x1F,0x00,0x01,0x84,0x30,0x80,0x01,0x82,0x61,0x00,0x01,0x82,0x40,0x00,0x01,0x81,0xC0,0x80,0x01,0x01,0x80,0x80,0x03,0x00,0x80,0x40,0x02,0x00,0x00,0x40,0x06,0x00,0x00,0x20,0x06,0x00,0x00,0x20,0x04,0x00,0x00,0x10,0x0C,0x00,0x00,0x10,0x08,0x00,0x00,0x10,0x18,0x08,0x08,0x08,0x10,0x18,0x18,0x08,0x30,0x1C,0x1C,0x04,0x60,0x3C,0x3C,0x02,0x70,0x2E,0x2E,0x06,0x7C,0x27,0x4E,0x3C,0x3F,0x27,0xC6,0xF0,0x07,0xC3,0x8F,0x80,0x01,0x83,0x06,0x00,
# 'N'
0x4E,0x09,0x17,0x15,0x00,0x17,
0x3F,0x07,0xFC,0xC1,0x10,0x07,0xC1,0x78,0x1F,0x81,0xF0,0x23,0x01,0xE0,0x46,0x01,0xC0,0x8C,0x01,0x81,0x18,0x01,0x02,0x30,0x00,0x04,0x60,0x00,0x08,0xC0,0x00,0x11,0x80,0x00,0x23,0x02,0x00,0x46,0x06,0x00,0x8C,0x0E,0x01,0x18,0x1E,0x02,0x30,0x3F,0x04,0x60,0x3F,0x0B,0x00,0x2F,0x17,0xFF,0x8F,0xEF,0xFE,0x0F,0x80,
# 'O'
0x4F,0x08,0x17,0x17,0x00,0x17,
0x00,0x7E,0x00,0x03,0x01,0x80,0x18,0x00,0x80,0x40,0x00,0x81,0x00,0x00,0x86,0x00,0x00,0x08,0x00,0x01,0x30,0x00,0x02,0x40,0x3C,0x03,0x80,0xFC,0x07,0x02,0x3C,0x0E,0x04,0x38,0x1C,0x08,0x30,0x3C,0x08,0x40,0x78,0x0F,0x01,0x30,0x00,0x02,0x70,0x00,0x08,0xF0,0x00,0x10,0xF0,0x00,0xC0,0xF0,0x03,0x00,0xFC,0x1C,0x00,0xFF,0xE0,0x00,0x3F,0x00,0x00,
# 'P'
0x50,0x09,0x13,0x15,0x00,0x13,
0x3F,0xFC,0x08,0x00,0x43,0x80,0x06,0x70,0x00,0x46,0x00,0x04,0xC0,0x00,0x18,0x00,0x0B,0x01,0x81,0x60,0x30,0x2C,0x04,0x05,0x80,0x00,0x30,0x00,0x26,0x00,0x08,0xC0,0x02,0x18,0x01,0x83,0x01,0xE0,0x60,0x30,0x08,0x04,0x03,0x00,0x80,0x7F,0xE0,0x07,0xF8,0x00,
# 'Q'
0x51,0x09,0x17,0x1C,0x00,0x17,
0x00,0x7E,0x00,0x03,0x01,0x00,0x18,0x00,0x80,0x40,0x00,0x81,0x00,0x00,0x86,0x00,0x01,0x08,0x00,0x01,0x30,0x1E,0x02,0x40,0x7E,0x03,0x81,0x1E,0x07,0x02,0x1C,0x0E,0x04,0x18,0x1C,0x04,0x20,0x3C,0x07,0x80,0x78,0x00,0x01,0x30,0x00,0x02,0x70,0x00,0x04,0xF0,0x00,0x10,0xF0,0x00,0x70,0xF0,0x00,0x00,0xFC,0x00,0x40,0xFF,0x81,0x00,0x3F,0x84,0x00,0x0F,0x10,0x00,0x06,0x40,0x00,0x0F,0x00,0x00,0x1C,0x00,0x00,0x00,0x00,
# 'R'
0x52,0x09,0x18,0x17,0x00,0x18,
0x3F,0xFE,0x00,0x60,0x01,0x80,0x70,0x00,0x40,0x70,0x00,0x20,0x30,0x00,0x20,0x30,0x00,0x10,0x30,0x10,0x10,0x30,0x18,0x10,0x30,0x10,0x10,0x30,0x00,0x10,0x30,0x00,0x20,0x30,0x00,0x20,0x30,0x00,0x10,0x30,0x00,0x1E,0x30,0x00,0x0A,0x30,0x18,0x06,0x30,0x1C,0x0C,0x20,0x0E,0x18,0x7F,0xFF,0x30,0x7F,0xE7,0x20,0x00,0x03,0xC0,0x00,0x03,0x80,0x00,0x03,0x00,
# 'S'
0x53,0x07,0x11,0x19,0x00,0x11,
0x00,0x06,0x00,0x02,0x80,0x1E,0x40,0x10,0x20,0x30,0x10,0x30,0x08,0x10,0x04,0x18,0x01,0x08,0x00,0x8C,0x0F,0x46,0x07,0xA3,0x01,0xE1,0xC0,0xE1,0xE0,0x41,0x70,0x21,0x80,0x10,0xC0,0x08,0x70,0x08,0x38,0x04,0x0C,0x04,0x06,0x04,0x03,0x3C,0x01,0xFC,0x00,0xF0,0x00,0x30,0x00,0x00,
# 'T'
0x54,0x08,0x12,0x16,0x01,0x13,
0x30,0x01,0x93,0xFF,0xDC,0x00,0x07,0x00,0x01,0xC0,0x00,0x70,0x00,0x1C,0x00,0x07,0x00,0x01,0xCC,0x07,0x7F,0x01,0xFF,0xC0,0x79,0xB0,0x1C,0x0C,0x04,0x03,0x01,0x00,0xC0,0x40,0x30,0x10,0x0C,0x04,0x03,0x01,0x00,0xC0,0x60,0x60,0x08,0x1F,0xFC,0x07,0xFE,0x00,
# 'U'
0x55,0x09,0x19,0x16,0xFF,0x18,
0x1F,0xF1,0xFF,0x10,0x05,0x00,0x9C,0x07,0xC0,0xCE,0x02,0xE0,0x43,0x01,0x30,0x21,0x80,0x98,0x10,0xC0,0x4C,0x08,0x60,0x26,0x04,0x30,0x13,0x02,0x18,0x09,0x81,0x0C,0x04,0xC0,0x86,0x02,0x60,0x43,0x01,0x30,0x21,0xC0,0x70,0x10,0xE0,0x00,0x10,0x30,0x00,0x08,0x1C,0x00,0x08,0x0F,0x00,0x08,0x03,0xC0,0x08,0x00,0xFC,0x18,0x00,0x1F,0xF8,0x00,0x03,0xF0,0x00,
# 'V'
0x56,0x07,0x19,0x18,0x00,0x19,
0x00,0xC1,0xC0,0x01,0x91,0x98,0x03,0x18,0xC3,0x06,0x04,0x60,0x64,0x02,0x20,0x1F,0x00,0xB0,0x1B,0xC0,0x70,0x0C,0xF0,0x10,0x08,0x38,0x00,0x08,0x0E,0x00,0x04,0x07,0x00,0x04,0x01,0xC0,0x06,0x00,0xE0,0x02,0x00,0x38,0x02,0x00,0x1C,0x01,0x00,0x07,0x01,0x00,0x03,0x81,0x80,0x00,0xE0,0x80,0x00,0x30,0x80,0x00,0x1C,0x40,0x00,0x06,0x40,0x00,0x03,0xE0,0x00,0x00,0xE0,0x00,0x00,0x60,0x00,
# 'W'
0x57,0x07,0x20,0x18,0x00,0x20,
0x00,0x60,0x03,0x80,0x01,0x90,0x06,0x60,0x0E,0x10,0xC6,0x1C,0x38,0x11,0xA6,0x07,0x60,0x11,0x26,0x01,0x78,0x12,0x1C,0x06,0x78,0x0E,0x1C,0x04,0x3C,0x0C,0x08,0x08,0x1C,0x00,0x08,0x10,0x0C,0x00,0x00,0x10,0x0E,0x00,0x00,0x20,0x06,0x00,0x00,0x20,0x07,0x00,0x00,0x40,0x03,0x00,0x00,0x40,0x03,0x80,0x00,0x80,0x03,0x80,0x00,0x80,0x01,0xC0,0x81,0x00,0x01,0xC1,0xC0,0x00,0x00,0xE1,0xC2,0x00,0x00,0xE2,0xE4,0x00,0x00,0x74,0xE4,0x00,0x00,0x7C,0x78,0x00,0x00,0x38,0x78,0x00,0x00,0x30,0x30,0x00,
# 'X'
0x58,0x05,0x19,0x1D,0x00,0x18,
0x00,0x01,0x80,0x00,0x01,0x20,0x00,0x61,0x8C,0x00,0x48,0xC3,0x00,0x44,0x40,0x60,0x43,0x60,0x10,0xC0,0xE0,0x18,0xC0,0x30,0x1C,0xC0,0x00,0x18,0x7C,0x00,0x08,0x1F,0x00,0x08,0x03,0x80,0x08,0x00,0xE0,0x04,0x00,0x38,0x02,0x00,0x0C,0x01,0x80,0x04,0x00,0x60,0x06,0x00,0x10,0x02,0x00,0x07,0x03,0x00,0x00,0x41,0x01,0x00,0x63,0x00,0xC0,0x62,0x00,0xF0,0x63,0x80,0x7C,0x61,0xF0,0x4E,0x60,0x7C,0x63,0xE0,0x0F,0x91,0xE0,0x01,0xF0,0x40,0x00,0x70,0x00,0x00,0x00,0x00,0x00,
# 'Y'
0x59,0x06,0x19,0x1B,0x00,0x19,
0x00,0x00,0x60,0x00,0xC0,0x48,0x00,0x80,0x62,0x00,0x88,0x20,0xC0,0x82,0x30,0x11,0x80,0xB0,0x01,0x80,0x30,0x0D,0x80,0x00,0x0C,0xF8,0x00,0x08,0x3E,0x00,0x04,0x07,0x80,0x04,0x01,0xE0,0x04,0x00,0x78,0x04,0x00,0x1C,0x02,0x00,0x0C,0x02,0x00,0x04,0x02,0x00,0x04,0x02,0x00,0x06,0x01,0x00,0x0E,0x01,0x00,0x0C,0x01,0x00,0x07,0x01,0x00,0x03,0xC0,0x80,0x01,0xF0,0x80,0x00,0x3E,0x00,0x00,0x0F,0xC0,0x00,0x03,0xE0,0x00,0x00,0x40,0x00,0x00,
# 'Z'
0x5A,0x08,0x13,0x17,0xFF,0x12,
0x0C,0x00,0x02,0xFF,0xFC,0xC0,0x01,0x98,0x00,0x23,0x00,0x04,0x60,0x01,0x0C,0x00,0x21,0x80,0x08,0x37,0x01,0x07,0xE0,0x60,0xF8,0x08,0x03,0x01,0x00,0x40,0x70,0x18,0x0D,0x02,0x00,0x20,0xC0,0x04,0x18,0x00,0x86,0x00,0x10,0xC0,0x02,0x10,0x00,0x47,0xFF,0xE8,0xFF,0xFE,0x00,0x01,0x80,
# '['
0x5B,0x04,0x0B,0x20,0x00,0x0B,
0x00,0x40,0x19,0xFD,0x60,0x2C,0x05,0x80,0xB0,0x16,0x0E,0xC1,0xD8,0x33,0x04,0x60,0x8C,0x11,0x82,0x30,0x46,0x08,0xC1,0x18,0x23,0x04,0x60,0x8C,0x11,0x82,0xB0,0x76,0x02,0xC0,0x58,0x0B,0x01,0x60,0x2F,0xFD,0xFF,0x80,0x60,0x00,
# '\'
0x5C,0x09,0x11,0x18,0x00,0x11,
0x3F,0x00,0x30,0x40,0x38,0x10,0x1E,0x08,0x0F,0x04,0x03,0x81,0x01,0xE0,0x80,0x70,0x20,0x3C,0x10,0x1E,0x08,0x07,0x02,0x03,0xC1,0x00,0xE0,0x40,0x78,0x20,0x3C,0x08,0x0F,0x04,0x07,0x82,0x01,0xC0,0x80,0xF0,0x40,0x38,0x10,0x1E,0x08,0x0F,0xFC,0x03,0xFC,0x01,0xFC,
# ']'
0x5D,0x04,0x0C,0x1F,0xFF,0x0B,
0x30,0x02,0xFF,0x60,0x16,0x01,0x60,0x16,0x01,0x60,0x16,0xC1,0x7C,0x16,0xC1,0x6C,0x10,0xC1,0x0C,0x10,0xC1,0x0C,0x10,0xC1,0x0C,0x10,0xC1,0x0C,0x10,0xC1,0x0C,0x13,0xC1,0x6C,0x16,0x01,0x60,0x16,0x01,0x60,0x16,0x01,0x7F,0xE7,0xFE,0x60,0x00,
# '^'
0x5E,0x1E,0x00,0x00,0x00,0x09,

# '_'
0x5F,0x20,0x10,0x04,0x00,0x10,
0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
# '`'
0x60,0x00,0x0A,0x09,0x00,0x0B,
0x00,0x06,0x02,0x61,0x8C,0x60,0xBF,0x17,0xFC,0x3E,0x03,0x00,
# 'a'
0x61,0x08,0x19,0x17,0x00,0x19,
0x00,0x0C,0x00,0x00,0x09,0x00,0x00,0x08,0x80,0x00,0x0C,0x20,0x00,0x04,0x08,0x00,0x06,0x04,0x00,0x02,0x01,0x00,0x03,0x00,0xC0,0x03,0x00,0x20,0x01,0x00,0x08,0x01,0x80,0x04,0x00,0x80,0x01,0x00,0xC0,0xC0,0x40,0xC0,0x60,0x20,0x40,0x00,0x08,0x60,0x00,0x06,0x40,0x00,0x00,0xF0,0x00,0x00,0xFE,0x1F,0xE1,0xCF,0xCF,0xF1,0x81,0xF4,0x1B,0x80,0x3E,0x0F,0x00,0x0E,0x06,0x00,
# 'b'
0x62,0x09,0x13,0x15,0x00,0x13,
0x3F,0xFC,0x0C,0x00,0x61,0xC0,0x06,0x38,0x00,0x43,0x00,0x04,0x60,0x60,0x8C,0x0C,0x11,0x81,0x02,0x30,0x00,0x46,0x00,0x08,0xC0,0x00,0x98,0x18,0x13,0x03,0x02,0x60,0x60,0x4C,0x00,0x09,0x80,0x01,0x30,0x00,0x44,0x00,0x11,0x80,0x0E,0x3F,0xFF,0x07,0xFF,0x80,
# 'c'
0x63,0x08,0x16,0x17,0x00,0x16,
0x00,0x7E,0x00,0x06,0x02,0x00,0x60,0x06,0x02,0x00,0x06,0x10,0x00,0x00,0xC0,0x00,0x22,0x00,0x01,0x18,0x0F,0x18,0x40,0x7E,0xC3,0x02,0x3E,0x0C,0x08,0xF0,0x30,0x21,0x80,0xC0,0x83,0x03,0x81,0x1A,0x0E,0x03,0xC4,0x18,0x00,0x08,0x70,0x00,0x19,0xE0,0x00,0x23,0xC0,0x01,0x87,0x80,0x1E,0x0F,0xC1,0xE0,0x0F,0xFE,0x00,0x0F,0xC0,0x00,
# 'd'
0x64,0x09,0x16,0x15,0xFF,0x15,
0x1F,0xFE,0x00,0x80,0x06,0x07,0x00,0x06,0x1C,0x00,0x0C,0x30,0x00,0x10,0xC0,0x00,0x23,0x00,0x00,0x8C,0x0F,0x01,0x30,0x3E,0x04,0xC0,0xF8,0x13,0x03,0xE0,0x4C,0x0F,0x01,0x30,0x00,0x04,0xC0,0x00,0x23,0x00,0x00,0x8C,0x00,0x04,0x30,0x00,0x20,0x80,0x01,0x06,0x00,0x18,0x1F,0xFF,0x80,0x3F,0xF0,0x00,
# 'e'
0x65,0x08,0x11,0x17,0x00,0x11,
0x00,0x01,0x0F,0xFF,0x48,0x00,0x2C,0x00,0x17,0x00,0x0B,0x80,0x04,0xC0,0x02,0x60,0x01,0x30,0x1A,0x98,0x01,0x8C,0x00,0x86,0x00,0x43,0x00,0x31,0x80,0xD4,0xC0,0x02,0x60,0x01,0x30,0x00,0x98,0x00,0x4C,0x00,0x24,0x00,0x17,0xFF,0xEB,0xFF,0xF8,0x00,0x08,
# 'f'
0x66,0x08,0x11,0x16,0xFF,0x10,
0x00,0x01,0x0F,0xFF,0x48,0x00,0x2E,0x00,0x17,0x00,0x09,0x80,0x04,0xC0,0x02,0x60,0x01,0x30,0x3A,0x98,0x01,0x8C,0x00,0xC6,0x00,0x43,0x00,0x21,0x81,0xD0,0xC0,0xF0,0x60,0x70,0x30,0x20,0x18,0x10,0x08,0x02,0x0C,0x01,0x07,0xFF,0x03,0xFF,0x00,
# 'g'
0x67,0x08,0x16,0x17,0x00,0x16,
0x00,0x7F,0x00,0x06,0x03,0x00,0x60,0x03,0x82,0x00,0x02,0x10,0x00,0x08,0xC0,0x00,0xC2,0x00,0x06,0x18,0x07,0x30,0x40,0x3C,0x83,0x01,0x3C,0x0C,0x04,0xFF,0xB0,0x14,0x02,0xC0,0x78,0x1B,0x80,0xE0,0x4E,0x01,0x81,0x18,0x00,0x04,0x70,0x00,0x11,0xE0,0x00,0x43,0xC0,0x01,0x07,0x80,0x18,0x0F,0x81,0xC0,0x1F,0xFC,0x00,0x0F,0xC0,0x00,
# 'h'
0x68,0x09,0x16,0x15,0x00,0x16,
0x3F,0xC7,0xF9,0x00,0xE0,0x1E,0x03,0xC0,0x98,0x0B,0x02,0x60,0x2C,0x09,0x80,0xF0,0x26,0x00,0x00,0x98,0x00,0x02,0x60,0x00,0x09,0x80,0x00,0x26,0x00,0x00,0x98,0x00,0x02,0x60,0x3C,0x09,0x80,0xF0,0x26,0x02,0xC0,0x98,0x0B,0x02,0x60,0x2C,0x09,0x00,0x20,0x1F,0xFF,0xFF,0xFF,0xF7,0xFC,0x00,0x00,0x00,
# 'i'
0x69,0x09,0x0B,0x15,0x00,0x0B,
0x3F,0xC8,0x07,0x81,0x70,0x26,0x04,0xC0,0x98,0x13,0x02,0x60,0x4C,0x09,0x81,0x30,0x26,0x04,0xC0,0x98,0x13,0x02,0x60,0x48,0x07,0x00,0xFF,0xEF,0xF8,
# 'j'
0x6A,0x09,0x0F,0x16,0x00,0x0F,
0x03,0xFC,0x08,0x04,0x38,0x08,0x70,0x10,0x60,0x20,0xC0,0x41,0x80,0x83,0x01,0x06,0x02,0x0C,0x04,0x18,0x08,0x30,0x10,0xA0,0x23,0x00,0x44,0x00,0x98,0x01,0x20,0x00,0xC0,0x09,0x00,0x27,0xC1,0x8F,0xFE,0x0F,0xF0,0x00,
# 'k'
0x6B,0x08,0x17,0x18,0x00,0x17,
0x00,0x01,0x80,0x7F,0xEE,0x81,0x80,0x38,0x87,0x81,0xE0,0x8F,0x03,0x80,0x86,0x06,0x00,0x8C,0x08,0x07,0x18,0x00,0x1C,0x30,0x00,0x70,0x60,0x01,0x00,0xC0,0x02,0x01,0x80,0x02,0x03,0x00,0x04,0x06,0x04,0x04,0x0C,0x0C,0x04,0x18,0x18,0x06,0x30,0x38,0x00,0x60,0x78,0x09,0x00,0x30,0x26,0x00,0x71,0x8F,0xFF,0xE4,0x0F,0xFC,0xD0,0x00,0x01,0xC0,0x00,0x00,0x00,
# 'l'
0x6C,0x09,0x11,0x16,0x00,0x11,
0x3F,0xF0,0x30,0x04,0x1C,0x06,0x0E,0x02,0x03,0x01,0x01,0x80,0x80,0xC0,0x40,0x60,0x20,0x30,0x10,0x18,0x08,0x0C,0x04,0xC6,0x03,0xD3,0x00,0x09,0x80,0x04,0xC0,0x02,0x60,0x01,0x30,0x00,0xB0,0x00,0x58,0x00,0x2F,0xFF,0xD7,0xFF,0xF0,0x00,0x30,
# 'm'
0x6D,0x09,0x20,0x16,0x00,0x1F,
0x00,0xF8,0x1F,0x00,0x01,0x84,0x30,0x80,0x01,0x82,0x61,0x00,0x01,0x82,0x40,0x00,0x01,0x81,0xC0,0x80,0x01,0x01,0x80,0x80,0x03,0x00,0x80,0x40,0x02,0x00,0x00,0x40,0x06,0x00,0x00,0x20,0x06,0x00,0x00,0x20,0x04,0x00,0x00,0x10,0x0C,0x00,0x00,0x10,0x08,0x00,0x00,0x10,0x18,0x08,0x08,0x08,0x10,0x18,0x18,0x08,0x30,0x1C,0x1C,0x04,0x60,0x3C,0x3C,0x02,0x70,0x2E,0x2E,0x06,0x7C,0x27,0x4E,0x3C,0x3F,0x27,0xC6,0xF0,0x07,0xC3,0x8F,0x80,0x01,0x83,0x06,0x00,
# 'n'
0x6E,0x09,0x17,0x15,0x00,0x17,
0x3F,0x07,0xFC,0xC1,0x10,0x07,0xC1,0x78,0x1F,0x81,0xF0,0x23,0x01,0xE0,0x46,0x01,0xC0,0x8C,0x01,0x81,0x18,0x01,0x02,0x30,0x00,0x04,0x60,0x00,0x08,0xC0,0x00,0x11,0x80,0x00,0x23,0x02,0x00,0x46,0x06,0x00,0x8C,0x0E,0x01,0x18,0x1E,0x02,0x30,0x3F,0x04,0x60,0x3F,0x0B,0x00,0x2F,0x17,0xFF,0x8F,0xEF,0xFE,0x0F,0x80,
# 'o'
0x6F,0x08,0x17,0x17,0x00,0x17,
0x00,0x7E,0x00,0x03,0x01,0x80,0x18,0x00,0x80,0x40,0x00,0x81,0x00,0x00,0x86,0x00,0x00,0x08,0x00,0x01,0x30,0x00,0x02,0x40,0x3C,0x03,0x80,0xFC,0x07,0x02,0x3C,0x0E,0x04,0x38,0x1C,0x08,0x30,0x3C,0x08,0x40,0x78,0x0F,0x01,0x30,0x00,0x02,0x70,0x00,0x08,0xF0,0x00,0x10,0xF0,0x00,0xC0,0xF0,0x03,0x00,0xFC,0x1C,0x00,0xFF,0xE0,0x00,0x3F,0x00,0x00,
# 'p'
0x70,0x09,0x13,0x15,0x00,0x13,
0x3F,0xFC,0x08,0x00,0x43,0x80,0x06,0x70,0x00,0x46,0x00,0x04,0xC0,0x00,0x18,0x00,0x0B,0x01,0x81,0x60,0x30,0x2C,0x04,0x05,0x80,0x00,0x30,0x00,0x26,0x00,0x08,0xC0,0x02,0x18,0x01,0x83,0x01,0xE0,0x60,0x30,0x08,0x04,0x03,0x00,0x80,0x7F,0xE0,0x07,0xF8,0x00,
# 'q'
0x71,0x09,0x17,0x1C,0x00,0x17,
0x00,0x7E,0x00,0x03,0x01,0x00,0x18,0x00,0x80,0x40,0x00,0x81,0x00,0x00,0x86,0x00,0x01,0x08,0x00,0x01,0x30,0x1E,0x02,0x40,0x7E,0x03,0x81,0x1E,0x07,0x02,0x1C,0x0E,0x04,0x18,0x1C,0x04,0x20,0x3C,0x07,0x80,0x78,0x00,0x01,0x30,0x00,0x02,0x70,0x00,0x04,0xF0,0x00,0x10,0xF0,0x00,0x70,0xF0,0x00,0x00,0xFC,0x00,0x40,0xFF,0x81,0x00,0x3F,0x84,0x00,0x0F,0x10,0x00,0x06,0x40,0x00,0x0F,0x00,0x00,0x1C,0x00,0x00,0x00,0x00,
# 'r'
0x72,0x09,0x18,0x17,0x00,0x18,
0x3F,0xFE,0x00,0x60,0x01,0x80,0x70,0x00,0x40,0x70,0x00,0x20,0x30,0x00,0x20,0x30,0x00,0x10,0x30,0x10,0x10,0x30,0x18,0x10,0x30,0x10,0x10,0x30,0x00,0x10,0x30,0x00,0x20,0x30,0x00,0x20,0x30,0x00,0x10,0x30,0x00,0x1E,0x30,0x00,0x0A,0x30,0x18,0x06,0x30,0x1C,0x0C,0x20,0x0E,0x18,0x7F,0xFF,0x30,0x7F,0xE7,0x20,0x00,0x03,0xC0,0x00,0x03,0x80,0x00,0x03,0x00,
# 's'
0x73,0x07,0x11,0x19,0x00,0x11,
0x00,0x06,0x00,0x02,0x80,0x1E,0x40,0x10,0x20,0x30,0x10,0x30,0x08,0x10,0x04,0x18,0x01,0x08,0x00,0x8C,0x0F,0x46,0x07,0xA3,0x01,0xE1,0xC0,0xE1,0xE0,0x41,0x70,0x21,0x80,0x10,0xC0,0x08,0x70,0x08,0x38,0x04,0x0C,0x04,0x06,0x04,0x03,0x3C,0x01,0xFC,0x00,0xF0,0x00,0x30,0x00,0x00,
# 't'
0x74,0x08,0x12,0x16,0x01,0x13,
0x30,0x01,0x93,0xFF,0xDC,0x00,0x07,0x00,0x01,0xC0,0x00,0x70,0x00,0x1C,0x00,0x07,0x00,0x01,0xCC,0x07,0x7F,0x01,0xFF,0xC0,0x79,0xB0,0x1C,0x0C,0x04,0x03,0x01,0x00,0xC0,0x40,0x30,0x10,0x0C,0x04,0x03,0x01,0x00,0xC0,0x60,0x60,0x08,0x1F,0xFC,0x07,0xFE,0x00,
# 'u'
0x75,0x09,0x19,0x16,0xFF,0x18,
0x1F,0xF1,0xFF,0x10,0x05,0x00,0x9C,0x07,0xC0,0xCE,0x02,0xE0,0x43,0x01,0x30,0x21,0x80,0x98,0x10,0xC0,0x4C,0x08,0x60,0x26,0x04,0x30,0x13,0x02,0x18,0x09,0x81,0x0C,0x04,0xC0,0x86,0x02,0x60,0x43,0x01,0x30,0x21,0xC0,0x70,0x10,0xE0,0x00,0x10,0x30,0x00,0x08,0x1C,0x00,0x08,0x0F,0x00,0x08,0x03,0xC0,0x08,0x00,0xFC,0x18,0x00,0x1F,0xF8,0x00,0x03,0xF0,0x00,
# 'v'
0x76,0x07,0x19,0x18,0x00,0x19,
0x00,0xC1,0xC0,0x01,0x91,0x98,0x03,0x18,0xC3,0x06,0x04,0x60,0x64,0x02,0x20,0x1F,0x00,0xB0,0x1B,0xC0,0x70,0x0C,0xF0,0x10,0x08,0x38,0x00,0x08,0x0E,0x00,0x04,0x07,0x00,0x04,0x01,0xC0,0x06,0x00,0xE0,0x02,0x00,0x38,0x02,0x00,0x1C,0x01,0x00,0x07,0x01,0x00,0x03,0x81,0x80,0x00,0xE0,0x80,0x00,0x30,0x80,0x00,0x1C,0x40,0x00,0x06,0x40,0x00,0x03,0xE0,0x00,0x00,0xE0,0x00,0x00,0x60,0x00,
# 'w'
0x77,0x07,0x20,0x18,0x00,0x20,
0x00,0x60,0x03,0x80,0x01,0x90,0x06,0x60,0x0E,0x10,0xC6,0x1C,0x38,0x11,0xA6,0x07,0x60,0x11,0x26,0x01,0x78,0x12,0x1C,0x06,0x78,0x0E,0x1C,0x04,0x3C,0x0C,0x08,0x08,0x1C,0x00,0x08,0x10,0x0C,0x00,0x00,0x10,0x0E,0x00,0x00,0x20,0x06,0x00,0x00,0x20,0x07,0x00,0x00,0x40,0x03,0x00,0x00,0x40,0x03,0x80,0x00,0x80,0x03,0x80,0x00,0x80,0x01,0xC0,0x81,0x00,0x01,0xC1,0xC0,0x00,0x00,0xE1,0xC2,0x00,0x00,0xE2,0xE4,0x00,0x00,0x74,0xE4,0x00,0x00,0x7C,0x78,0x00,0x00,0x38,0x78,0x00,0x00,0x30,0x30,0x00,
# 'x'
0x78,0x05,0x19,0x1D,0x00,0x18,
0x00,0x01,0x80,0x00,0x01,0x20,0x00,0x61,0x8C,0x00,0x48,0xC3,0x00,0x44,0x40,0x60,0x43,0x60,0x10,0xC0,0xE0,0x18,0xC0,0x30,0x1C,0xC0,0x00,0x18,0x7C,0x00,0x08,0x1F,0x00,0x08,0x03,0x80,0x08,0x00,0xE0,0x04,0x00,0x38,0x02,0x00,0x0C,0x01,0x80,0x04,0x00,0x60,0x06,0x00,0x10,0x02,0x00,0x07,0x03,0x00,0x00,0x41,0x01,0x00,0x63,0x00,0xC0,0x62,0x00,0xF0,0x63,0x80,0x7C,0x61,0xF0,0x4E,0x60,0x7C,0x63,0xE0,0x0F,0x91,0xE0,0x01,0xF0,0x40,0x00,0x70,0x00,0x00,0x00,0x00,0x00,
# 'y'
0x79,0x06,0x19,0x1B,0x00,0x19,
0x00,0x00,0x60,0x00,0xC0,0x48,0x00,0x80,0x62,0x00,0x88,0x20,0xC0,0x82,0x30,0x11,0x80,0xB0,0x01,0x80,0x30,0x0D,0x80,0x00,0x0C,0xF8,0x00,0x08,0x3E,0x00,0x04,0x07,0x80,0x04,0x01,0xE0,0x04,0x00,0x78,0x04,0x00,0x1C,0x02,0x00,0x0C,0x02,0x00,0x04,0x02,0x00,0x04,0x02,0x00,0x06,0x01,0x00,0x0E,0x01,0x00,0x0C,0x01,0x00,0x07,0x01,0x00,0x03,0xC0,0x80,0x01,0xF0,0x80,0x00,0x3E,0x00,0x00,0x0F,0xC0,0x00,0x03,0xE0,0x00,0x00,0x40,0x00,0x00,
# 'z'
0x7A,0x08,0x13,0x17,0xFF,0x12,
0x0C,0x00,0x02,0xFF,0xFC,0xC0,0x01,0x98,0x00,0x23,0x00,0x04,0x60,0x01,0x0C,0x00,0x21,0x80,0x08,0x37,0x01,0x07,0xE0,0x60,0xF8,0x08,0x03,0x01,0x00,0x40,0x70,0x18,0x0D,0x02,0x00,0x20,0xC0,0x04,0x18,0x00,0x86,0x00,0x10,0xC0,0x02,0x10,0x00,0x47,0xFF,0xE8,0xFF,0xFE,0x00,0x01,0x80,
# '{'
0x7B,0x05,0x0D,0x1F,0x01,0x0E,
0x00,0x10,0x0E,0x81,0x04,0x10,0x21,0x81,0x08,0x08,0xC0,0x46,0x0E,0x30,0x71,0x83,0x0C,0x10,0x60,0x84,0x04,0x60,0x23,0x02,0x18,0x08,0xC0,0x47,0x82,0x3C,0x10,0x60,0x83,0x05,0x18,0x38,0xC0,0x46,0x02,0x38,0x11,0xC0,0x87,0x84,0x1F,0xE0,0x7F,0x00,0x30,0x00,0x00,
# '|'
0x7C,0x1E,0x00,0x00,0x00,0x09,

# '}'
0x7D,0x04,0x0E,0x1F,0x00,0x0F,
0x30,0x00,0xBC,0x06,0x0C,0x18,0x08,0x60,0x21,0x80,0x46,0x01,0x1F,0x04,0x7C,0x11,0xB0,0x44,0xC1,0x03,0x04,0x0C,0x0C,0x30,0x10,0xE0,0x43,0x81,0x04,0x04,0x30,0x70,0xC1,0x03,0x04,0x0C,0x10,0xF0,0x46,0xC1,0x18,0x04,0x60,0x11,0x80,0x86,0x04,0x18,0x60,0x7F,0x81,0xF8,0x06,0x00,0x00,
# '~'
0x7E,0x1E,0x00,0x00,0x00,0x09,


# Terminator
0xFF
]
