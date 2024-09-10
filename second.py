from manim import *

class SolveQuadraticEquation(Scene):
    def construct(self):
        # Introduction générale
        self.introduction()

        # Partie théorique avec la démonstration complète des 9 étapes
        self.theory_section()

        # Ajout de l'explication de pourquoi \( \Delta = b^2 - 4ac \)
        self.explanation_of_delta()

        # Ajout du résumé des solutions pour \( \Delta > 0 \) et \( \Delta = 0 \)
        self.summary_of_solutions()

        # Exemple 1 : Delta > 0 (deux solutions réelles)
        self.example_positive_discriminant()

        # Effacer tout avant le deuxième exemple
        self.clear_before_second_example()

        # Exemple 2 : Delta = 0 (une solution réelle)
        self.example_zero_discriminant()

        # Rappel des astuces
        self.reminder()

        # Message final d'encouragement
        self.final_message()

    def introduction(self):
        # Introduction au début de la vidéo
        intro_text = Tex(r"Comment résoudre une équation du second degré ?").scale(0.9).move_to(ORIGIN)
        intro_text_2 = Tex(r"Voyons ensemble comment déterminer les solutions réelles.").scale(0.9).move_to(ORIGIN)

        self.play(Write(intro_text))
        self.wait(2)
        self.play(Transform(intro_text, intro_text_2))
        self.wait(2)
        self.play(FadeOut(intro_text))

    def theory_section(self):
        # Étape 1 : Présentation initiale de l'équation
        equation = MathTex(r"ax^2 + bx + c = 0").move_to(ORIGIN)
        self.play(Write(equation))
        self.wait(2)

        # Étape 2 : Factoriser \(a\) à gauche
        equation_factor_a = MathTex(r"a\left(x^2 + \frac{b}{a}x + \frac{c}{a}\right) = 0").move_to(ORIGIN)
        self.play(Transform(equation, equation_factor_a))
        self.wait(2)

        # Étape 3 : Suppression du coefficient \(a\) car \(a \neq 0\)
        equation_simplified = MathTex(r"x^2 + \frac{b}{a}x + \frac{c}{a} = 0").move_to(ORIGIN)
        self.play(Transform(equation, equation_simplified))
        self.wait(2)

        # Étape 4 : Compléter le carré \(x^2 + \frac{b}{a}x\)
        equation_complete_square = MathTex(r"x^2 + 2 \cdot \frac{b}{2a}x + \frac{b^2}{4a^2} - \frac{b^2}{4a^2} + \frac{c}{a} = 0").move_to(ORIGIN)
        self.play(Transform(equation, equation_complete_square))
        self.wait(2)

        # Étape 5 : Regrouper sous forme de carrés parfaits
        equation_perfect_square = MathTex(r"\left(x + \frac{b}{2a}\right)^2 - \frac{b^2}{4a^2} + \frac{c}{a} = 0").move_to(ORIGIN)
        self.play(Transform(equation, equation_perfect_square))
        self.wait(2)

        # Étape 6 : Simplification des fractions
        equation_simplify_fractions = MathTex(r"\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2}").move_to(ORIGIN)
        self.play(Transform(equation, equation_simplify_fractions))
        self.wait(2)

        # Étape 7 : Prendre la racine carrée des deux côtés
        # Ajout de la racine carrée visuelle
        equation_with_sqrt = MathTex(r"\sqrt{\left(x + \frac{b}{2a}\right)^2} = \pm \sqrt{\frac{b^2 - 4ac}{4a^2}}").move_to(ORIGIN)
        self.play(Transform(equation, equation_with_sqrt))
        self.wait(2)

        # Simplification du carré et de la racine
        equation_sqrt_simplified = MathTex(r"x + \frac{b}{2a} = \pm \frac{\sqrt{b^2 - 4ac}}{2a}").move_to(ORIGIN)
        self.play(Transform(equation, equation_sqrt_simplified))
        self.wait(2)

        # Étape 8 : Isoler \(x\)
        equation_isolate_x = MathTex(r"x + \frac{b}{2a} = \pm \frac{\sqrt{b^2 - 4ac}}{2a}").move_to(ORIGIN)
        self.play(Transform(equation, equation_isolate_x))
        self.wait(2)

        # Étape 9 : Solution finale de l'équation
        equation_final = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").move_to(ORIGIN)
        self.play(Transform(equation, equation_final))
        self.wait(5)
        self.play(FadeOut(equation, equation_final))

    def explanation_of_delta(self):
        # Explication de pourquoi \( \Delta = b^2 - 4ac \)
        explanation = Tex(r"Le discriminant est donné par :").move_to(UP)
        delta_formula = MathTex(r"\Delta = b^2 - 4ac").move_to(DOWN)
        
        self.play(Write(explanation))
        self.wait(2)
        self.play(Write(delta_formula))
        self.wait(2)
        self.play(FadeOut(explanation, delta_formula))

    def summary_of_solutions(self):
        # Partie pour \( \Delta > 0 \) à gauche
        delta_greater_than_zero = VGroup(
            Tex("Si "), MathTex(r"\Delta > 0")
        ).arrange(RIGHT).move_to(UP * 2 + LEFT * 4)

        two_solutions_text = Tex(r"Deux solutions :").next_to(delta_greater_than_zero, DOWN, buff=0.5)
        solution_x1 = MathTex(r"x_1 = \frac{-b + \sqrt{\Delta}}{2a}").next_to(two_solutions_text, DOWN, buff=0.5)
        solution_x2 = MathTex(r"x_2 = \frac{-b - \sqrt{\Delta}}{2a}").next_to(solution_x1, DOWN, buff=0.5)

        # Partie pour \( \Delta = 0 \) à droite
        delta_equals_zero = VGroup(
            Tex("Si "), MathTex(r"\Delta = 0")
        ).arrange(RIGHT).move_to(UP * 2 + RIGHT * 4)

        one_solution_text = Tex(r"Une solution (racine double) :").next_to(delta_equals_zero, DOWN, buff=0.5)
        solution_x = MathTex(r"x = \frac{-b}{2a}").next_to(one_solution_text, DOWN, buff=0.5)

        # Créer une ligne de séparation entre les deux parties
        separator_line = Line(UP * 2.5 + ORIGIN, DOWN * 2.5 + ORIGIN, stroke_width=2)

        # Affichage des éléments
        self.play(Write(separator_line))
        self.play(Write(delta_greater_than_zero), Write(two_solutions_text), Write(solution_x1), Write(solution_x2))
        self.play(Write(delta_equals_zero), Write(one_solution_text), Write(solution_x))
        self.wait(8)
        self.play(FadeOut(separator_line, delta_greater_than_zero, two_solutions_text, solution_x1, solution_x2, delta_equals_zero, one_solution_text, solution_x))

    def example_positive_discriminant(self):
        # Exemple d'équation avec Delta > 0
        example_title = Tex("Exemple 1 : Deux solutions réelles ").scale(0.9)
        delta_math = MathTex(r"(\Delta > 0)").next_to(example_title, RIGHT)
        self.play(Write(example_title))
        self.play(Write(delta_math))
        self.wait(2)
        self.play(FadeOut(example_title, delta_math))

        equation = MathTex(r"x^2 - 3x + 2 = 0").move_to(ORIGIN)
        self.play(Write(equation))
        self.wait(2)

        # Ajout des valeurs de a, b, c
        abc_values = Tex(r"où $a = 1$, $b = -3$, $c = 2$").next_to(equation, DOWN, buff=0.5)
        self.play(Write(abc_values))
        self.wait(2)

        # Calcul du discriminant
        discriminant_calc = MathTex(r"\Delta = (-3)^2 - 4 \cdot 1 \cdot 2 = 9 - 8 = 1").move_to(ORIGIN)
        self.play(Transform(equation, discriminant_calc))
        self.play(FadeOut(abc_values))
        self.wait(2)
        self.play(FadeOut(equation))

        # Afficher les solutions \(x_1\) et \(x_2\) l'une sous l'autre
        solution_x1 = MathTex(r"x_1 = \frac{-(-3) + \sqrt{1}}{2 \cdot 1} = \frac{3 + 1}{2 } = \frac{4 }{2 }=  2").move_to(UP)
        solution_x2 = MathTex(r"x_2 = \frac{-(-3) - \sqrt{1}}{2 \cdot 1} = \frac{3 - 1}{2 } = \frac{2 }{2 }=  1").move_to(DOWN)
        self.play(Write(solution_x1))
        self.play(Write(solution_x2))
        self.wait(2)

        # Afficher le résultat final simplifié
        final_result = Tex(r"Les solutions sont : $x_1 = 2$, $x_2 = 1$").move_to(ORIGIN)
        self.play(Transform(VGroup(solution_x1, solution_x2), final_result))
        self.wait(2)

        # Effacer avant de passer au deuxième exemple
        self.fade_out_elements([final_result])

        # Effacer avant de passer au deuxième exemple
        self.fade_out_elements([final_result])

    def clear_before_second_example(self):
        # Effacer avant le deuxième exemple
        self.play(FadeOut(*self.mobjects))
        second_example_intro = VGroup(
            Tex("Exemple 2 : Une solution réelle "), 
            MathTex(r"(\Delta = 0)")
        ).arrange(RIGHT).move_to(ORIGIN)
        self.play(Write(second_example_intro))
        self.wait(2)
        self.play(FadeOut(second_example_intro))

    def example_zero_discriminant(self):
        # Exemple d'équation avec Delta = 0
        equation = MathTex(r"x^2 - 4x + 4 = 0").move_to(ORIGIN)
        self.play(Write(equation))
        self.wait(2)

        # Ajout des valeurs de a, b, c
        abc_values = Tex(r"où $a = 1$, $b = -4$, $c = 4$").next_to(equation, DOWN, buff=0.5)
        self.play(Write(abc_values))
        self.wait(2)

        # Calcul du discriminant
        discriminant_calc = MathTex(r"\Delta = (-4)^2 - 4 \cdot 1 \cdot 4 = 16 - 16 = 0").move_to(ORIGIN)
        self.play(Transform(equation, discriminant_calc))
        self.play(FadeOut(abc_values))
        self.wait(2)
        self.play(FadeOut(equation))

        # Afficher la solution \(x\) avec le résultat final simplifié
        solution_x = MathTex(r"x = \frac{-(-4)}{2 \cdot 1} = \frac{4 }{2 } = 2").move_to(ORIGIN)
        self.play(Write(solution_x))
        self.wait(2)

        # Afficher le résultat final simplifié
        final_result = Tex(r"La solution est : $x = 2$").move_to(ORIGIN)
        self.play(Transform(solution_x, final_result))
        self.wait(2)

        self.fade_out_elements([final_result, solution_x])

    def reminder(self):
        # Rappel des astuces pour bien résoudre une équation du second degré
        reminder_text = Tex(r"Rappel : Astuces pour résoudre une équation du second degré").scale(0.9).move_to(ORIGIN)
        self.play(Write(reminder_text))
        self.wait(2)
        self.play(FadeOut(reminder_text))

        # Liste des astuces
        tips = [
            Tex(r"1. Identifiez les coefficients \(a\), \(b\), et \(c\).").scale(0.9).move_to(ORIGIN),
            Tex(r"2. Calculez le discriminant \(\Delta = b^2 - 4ac\).").scale(0.9).move_to(ORIGIN),
            Tex(r"3. Utilisez la formule pour trouver les solutions.").scale(0.9).move_to(ORIGIN),
            Tex(r"4. Si \(\Delta > 0\), deux solutions ; si \(\Delta = 0\), une solution.").scale(0.9).move_to(ORIGIN)
        ]

        for tip in tips:
            self.play(Write(tip))
            self.wait(2)
            self.play(FadeOut(tip))

    def final_message(self):
        # Message final d'encouragement et de remerciement
        final_text = VGroup(
            Tex(r"Merci d'avoir regardé !").scale(0.9),
            Tex(r"Bonne chance avec vos équations du second degré !").scale(0.9)
        ).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        self.play(Write(final_text))
        self.wait(3)
        self.play(FadeOut(final_text))

    def fade_out_elements(self, elements):
        # Effectue un fade out sur tous les éléments donnés
        self.play(*[FadeOut(element) for element in elements if element is not None])