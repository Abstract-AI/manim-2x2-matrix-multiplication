from manim import *
import numpy as np
class matrixTest(Scene):
	
	def construct(self):
		A = np.array([[-1, 5], [7, 11]])
		B = np.array([[2, 3], [-8, 0]])
		C = np.dot(A, B)
		
		stuff = VGroup(Matrix(A), Matrix(B), Matrix(C))
		matrixA = stuff[0]
		matrixB = stuff[1]
		matrixC = stuff[2]
		matrixA.height = 2.5
		matrixB.height = 2.5
		matrixA.color = PURPLE
		matrixB.color = RED
		Dot = Tex(".", color=WHITE, font_size = 200)
		Equals = Tex("=", color=WHITE, font_size = 100)
		bOpen = Tex("[", color=WHITE, font_size = 100)
		bClose = Tex("]", color=WHITE, font_size=100)
		bOpen1 = Tex("[", color=WHITE, font_size=200)
		bClose1 = Tex("]", color=WHITE, font_size=200)
		
		
		self.play(Write(matrixA))
		self.play(matrixA.animate.scale(1).to_corner(UP+LEFT*2))
		
		Dot.next_to(matrixA, RIGHT)
		self.play(Write(Dot))
		
		self.play(Write(matrixB))
		self.play(matrixB.animate.scale(1).next_to(Dot, RIGHT))
		
		Equals.next_to(matrixB, RIGHT)
		self.play(Write(Equals))
		
		matrixC.next_to(Equals)
		C_elements = VGroup(*matrixC)
		for i in C_elements[1:]:
			i.height = 2.5
			self.play(Write(i))
		C_elements = VGroup(*C_elements[0])
		A_rows = matrixA.get_rows()
		A = VGroup(A_rows[0], A_rows[0], A_rows[1], A_rows[1])
		B_columns = matrixB.get_columns()
		B = VGroup(B_columns[0], B_columns[1], B_columns[0], B_columns[1])
		
		for r, c, ans in zip(A.copy(), B.copy(), C_elements.copy()):
			_bOpen = bOpen.copy()
			_bClose = bClose.copy()
			_bOpen1 = bOpen1.copy()
			_bClose1 = bClose1.copy()
			_Dot = Dot.copy()
			_r = r.copy()
			_c = c.copy()
			_bOpen.next_to(matrixA, DOWN*3)
			self.play(Write(_bOpen))
			self.play(_r.set_color(BLUE).animate.next_to(_bOpen))
			_bClose.next_to(_r, RIGHT)
			self.play(Write(_bClose))
			_Dot.next_to(_bClose, RIGHT)
			self.play(Write(_Dot))
			_bOpen1.next_to(_Dot, RIGHT)
			self.play(Write(_bOpen1))
			self.play(_c.set_color(YELLOW).animate.next_to(_bOpen1))
			_bClose1.next_to(_c, RIGHT)
			self.play(Write(_bClose1))
			g = VGroup(_bOpen, _r, _bClose, _Dot, _bOpen1, _c, _bClose1)
			ans.font_size = 60
			ans.set_color(PURE_GREEN)
			self.play(Transform(g, ans))
			
		self.wait()
		self.play(Write(Text("Code in the desciption", font_size=80)))
		self.wait()
		
