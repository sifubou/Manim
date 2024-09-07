from manim import *

class Adam2(Scene):
    def construct(self):
        # Introduction générale
        self.introduction()

        # Partie théorique avec exemples
        self.theory_section()

        # Premier exemple pratique
        self.example_section()

        # FadeOut entre les deux exemples
        self.clear_before_second_example()

        # Deuxième exemple pratique avec X des deux côtés de l'équation
        self.second_example_section()

        # Rappel des astuces pour bien résoudre une équation
        self.reminder()

        # Message d'encouragement et de remerciement
        self.final_message()

    def introduction(self):
        # Introduction au début de la vidéo
        intro_text = Tex(r"Vous vous êtes déjà demandé comment résoudre une équation ?").scale(0.9)
        intro_text_2 = Tex(r"Peut-être que vous ne savez pas par où commencer ?").scale(0.9)
        intro_text_3 = Tex(r"Alors cette vidéo est faite pour vous !").scale(0.9)

        self.play(Write(intro_text))
        self.wait(2)
        self.play(Transform(intro_text, intro_text_2))
        self.wait(2)
        self.play(Transform(intro_text, intro_text_3))
        self.wait(2)
        self.play(FadeOut(intro_text))

    def theory_section(self):
        # Partie théorique inchangée
        intro = Tex(r"Résoudre une équation : étapes générales").scale(0.9)
        self.play(Write(intro))
        self.wait(2)
        self.play(FadeOut(intro))

        step1 = Tex(r"Étape 1 : Identifier les termes.").scale(0.8)
        step1.to_edge(UP)
        self.play(Write(step1))
        self.wait(1)

        example1 = MathTex(r"3x", r"+", r"5", r"=", r"14").move_to(ORIGIN)
        self.play(Write(example1))
        self.wait(2)

        self.play(
            example1[0].animate.set_color(YELLOW),  # '3x' en jaune
            example1[2].animate.set_color(BLUE),    # '5' en bleu
            example1[4].animate.set_color(BLUE)     # '14' en rouge
        )
        self.wait(2)

        self.fade_out_elements([step1, example1])

        step2 = Tex(r"Étape 2 : Regrouper les termes similaires.").scale(0.8)
        step2.to_edge(UP)
        self.play(Write(step2))
        self.wait(1)

        example2 = MathTex(r"3x", r"+", r"5", r" - 5", r"=", r"14", r" - 5").move_to(ORIGIN)
        example2.set_color_by_tex(" - 5", YELLOW)
        self.play(Write(example2))
        self.wait(2)

        simplified_example2 = MathTex(r"3x = 9").move_to(ORIGIN)
        self.play(Transform(example2, simplified_example2))
        self.wait(2)

        self.fade_out_elements([step2, example2])

        step4 = Tex(r"Étape 3 : Simplifier l'équation avec les opérations inverses.").scale(0.8)
        step4.to_edge(UP)
        self.play(Write(step4))
        self.wait(1)

        example4 = MathTex(r"3x = 9").move_to(ORIGIN)
        self.play(Write(example4))
        self.wait(1)

        divide_example4 = MathTex(r"\frac{3x}{3} = \frac{9}{3}").move_to(ORIGIN)
        divide_example4.set_color_by_tex("/ 5", YELLOW)
        self.play(Transform(example4, divide_example4))
        self.wait(2)

        self.fade_out_elements([step4, divide_example4, example4])

        conclusion = Tex(r"Suivez ces étapes pour résoudre toute équation.").scale(0.8)
        self.play(Write(conclusion))
        self.wait(2)
        self.play(FadeOut(conclusion))

    def example_section(self):
        # Exemple pratique 1 : 2x + 3 = 7
        example_intro = Tex(r"Exemple pratique : Résolution d'une équation").scale(0.9)
        self.play(Write(example_intro))
        self.wait(2)
        self.play(FadeOut(example_intro))

        example1 = MathTex(r"2x + 3 = 7").move_to(ORIGIN)
        self.play(Write(example1))
        self.wait(2)

        step1 = Tex(r"Étape 1 : Soustraire 3 des deux côtés").scale(0.8)
        step1.to_edge(UP)
        self.play(Write(step1))
        self.wait(1)

        self.play(Transform(example1, MathTex(r"2x + 3 - 3 = 7 - 3").move_to(ORIGIN)))
        self.wait(2)

        self.play(FadeOut(step1))
        step2 = MathTex(r"\text{Étape 2 : Simplification en } 2x = 4").scale(0.8)
        step2.to_edge(UP)
        self.play(Write(step2))

        self.play(Transform(example1, MathTex(r"2x = 4").move_to(ORIGIN)))
        self.wait(2)

        self.play(FadeOut(step2))
        step3 = Tex(r"Étape 3 : Diviser chaque côté par 2").scale(0.8)
        step3.to_edge(UP)
        self.play(Write(step3))

        self.play(Transform(example1, MathTex(r"\frac{2x}{2} = \frac{4}{2}").move_to(ORIGIN)))
        self.wait(2)

        self.play(FadeOut(step3))
        self.play(Transform(example1, MathTex(r"x = 2").scale(0.9).move_to(ORIGIN)))
        self.wait(2)

    def clear_before_second_example(self):
        # FadeOut pour supprimer tout avant l'exemple 2
        self.play(FadeOut(*self.mobjects))
        second_example_intro = Tex(r"Passons maintenant au deuxième exemple").scale(0.9)
        self.play(Write(second_example_intro))
        self.wait(2)
        self.play(FadeOut(second_example_intro))

    def second_example_section(self):
        # Deuxième exemple pratique avec X des deux côtés de l'équation
        second_intro = MathTex(r"\text{Deuxième exemple : Résolution d'une équation avec } x \text{ des deux côtés}").scale(0.9)

        self.play(Write(second_intro))
        self.wait(2)
        self.play(FadeOut(second_intro))

        example2 = MathTex(r"3x + 5 = 2x + 10").move_to(ORIGIN)
        self.play(Write(example2))
        self.wait(2)

        step1 = MathTex(r"\text{Étape 1 : Soustraire } 2x \text{ des deux côtés}").scale(0.8)
        step1.to_edge(UP)
        self.play(Write(step1))
        self.wait(1)

        self.play(Transform(example2, MathTex(r"3x - 2x + 5 = 2x - 2x + 10").move_to(ORIGIN)))
        self.wait(2)

        self.play(FadeOut(step1))
        step2 = MathTex(r"\text{Étape 2 : Simplification en } x + 5 = 10").scale(0.8)
        step2.to_edge(UP)
        self.play(Write(step2))

        self.play(Transform(example2, MathTex(r"x + 5 = 10").move_to(ORIGIN)))
        self.wait(2)

        self.play(FadeOut(step2))
        step3 = Tex(r"Étape 3 : Soustraire 5 des deux côtés").scale(0.8)
        step3.to_edge(UP)
        self.play(Write(step3))

        self.play(Transform(example2, MathTex(r"x + 5 - 5 = 10 - 5").move_to(ORIGIN)))
        self.wait(2)

        self.play(FadeOut(step3))
        self.play(Transform(example2, MathTex(r"x = 5").scale(0.9).move_to(ORIGIN)))
        self.wait(2)

        # Effacer l'équation avant de passer au rappel
        self.play(FadeOut(example2))

    def reminder(self):
        # Rappel des astuces pour bien résoudre une équation
        reminder_text = Tex(r"Rappel : Astuces pour bien résoudre une équation").scale(0.9)
        self.play(Write(reminder_text))
        self.wait(2)
        self.play(FadeOut(reminder_text))

        # Liste des étapes
        tips = [
            Tex(r"1. Identifiez les termes à regrouper.").scale(0.9),
            MathTex(r"\text{2. Regroupez les } x \text{ d'un côté et les constantes de l'autre.}").scale(0.9),
            Tex(r"3. Simplifiez l'équation étape par étape.").scale(0.9),
            Tex(r"4. Utilisez les opérations inverses (addition, soustraction, division, multiplication).").scale(0.9),
            Tex(r"5. Ne sautez pas d'étapes, même si elles semblent simples.").scale(0.9)
        ]

        # Afficher chaque étape une par une et effacer l'étape précédente
        for tip in tips:
            self.play(Write(tip.move_to(ORIGIN)))
            self.wait(2)
            self.play(FadeOut(tip))

    def final_message(self):
        # Message d'encouragement et de remerciement à la fin
        final_text = VGroup(
            Tex(r"Merci d'avoir regardé !").scale(0.9),
            Tex(r"Bonne chance avec vos équations !").scale(0.9)
        ).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        self.play(Write(final_text))
        self.wait(3)
        self.play(FadeOut(final_text))


    def fade_out_elements(self, elements):
        # Effectue un fade out sur tous les éléments donnés
        self.play(*[FadeOut(element) for element in elements if element is not None])