#!/usr/bin/env python
import os
from cvmaker import CV

# Sample CV (mine)

def set_banner(cv):
    cv.set_photo("CV_photo.png")
    cv.set_name("Bruno M. Ronchi")
    cv.set_title("M.Sc. in Physics")
    cv.add_id_data("Age: 26 (1994)")
    cv.add_id_data("E-mail: brunom.ronchi@gmail.com")
    cv.add_id_data("Currently in: Junín, Buenos Aires, Argentina.")
    cv.add_id_data("Reallocation is a non-issue.")

def add_IB_MSc(cv):
    cv.add_text(CV().Text("Aug. 2019 - Feb. 2021,"
                            "in Balseiro Institute, Argentina", weight='bold'))
    cv.add_text(CV().Text("M.Sc. in Physics", weight='bold'))
    cv.tab()
    cv.step()
    cv.add_text(CV().Text('Thesis:', weight='bold')+
                CV().Text(' "Amplifying information of quantum sensors'
                            ' with Quantum Zeno Effect"'))
    cv.add_text(CV().Text('Advisor:', weight='bold')+
                CV().Text(' Dr. Gonzalo Agustín Álvarez.'))
    cv.add_text(CV().Text('Tutor:', weight='bold')+
                CV().Text(' Dr. Analía Zwick.'))
    cv.add_text(CV().Text('Nuclear Magnetic Resonance Spectroscopy '
                          'and Imaging Laboratory,', weight='bold'))
    cv.add_text('Medical Physics Department, Bariloche Atomic Center.')
    cv.add_text('Bariloche Atomic Center.')
    cv.add_text(CV().Text('Acquired knowledges:', weight='bold')+
                CV().Text(' mainly on the fields of '
                          '(quantum) parameter estimation.'))
    cv.add_text('Also include OOP (C++), parallel programming (CUDA/OpenCL),'
                'probability')
    cv.add_text('theory, information theory, and fundamentals of '
                'machine learning.')
    cv.tab(-1)
    cv.step(2.5)

def add_IB_BSc(cv):
    cv.add_text(CV().Text("Aug. 2016 - Dec. 2020,"
                            "in Balseiro Institute, Argentina", weight='bold'))
    cv.add_text(CV().Text("B.Sc. in Physics", weight='bold'))
    cv.tab()
    cv.step()
    cv.add_text(CV().Text('Thesis:', weight='bold')+
                CV().Text(' "Amplifying information of quantum sensors'
                            ' with Quantum Zeno Effect"'))
    cv.add_text(CV().Text('Advisor:', weight='bold')+
                CV().Text(' Dr. Gonzalo Agustín Álvarez.'))
    cv.add_text(CV().Text('Tutor:', weight='bold')+
                CV().Text(' Dr. Analía Zwick.'))
    cv.add_text(CV().Text('Nuclear Magnetic Resonance Spectroscopy '
                          'and Imaging Laboratory,', weight='bold'))
    cv.add_text('Medical Physics Department, Bariloche Atomic Center.')
    cv.add_text(CV().Text('Acquired knowledges:', weight='bold')+
            CV().Text(' mathematical reasoning, fundamentals of physics:'))
    cv.add_text('Classical Mechanics, Thermodynamics, Statistical Mechanics, '
                'Electromagnetism,')
    cv.add_text('and Quantum Mechanics. Programming (C), '
                'experimental research skills.')
    cv.add_text(CV().Text('Average score:', weight='bold')+
                CV().Text(' 8.00, scale from 0 (worst) to 10 (best).'))
    cv.tab(-1)
    cv.step(2.5)

def add_FCEIA_BSc(cv):
    cv.add_text(CV().Text('Feb. 2013 - June 2016, in National University of '
                          'Rosario, Argentina', weight='bold'))
    cv.tab()
    cv.step()
    cv.add_text(CV().Text('First years of B.Sc. in physics,', weight='bold')+
                CV().Text('validating the subjects pre-required for entry at'))
    cv.add_text('the Balseiro institute.')
    cv.tab(-1)
    cv.step(2.5)

def add_languages(cv):
    cv.add_text(CV().Text('Languages', weight='bold'))
    cv.tab()
    cv.step()
    cv.add_text('Spanish (Native), English (Fluent), C and C++, Python, LaTeX.')
    cv.tab(-1)
    cv.step(2.5)

def add_scholarships(cv):
    cv.add_text(CV().Text('Scholarships through my studies', weight='bold'))
    cv.tab()
    cv.step()
    cv.add_text('Complete scholarship during the M.Sc. in Balseiro Institute.')
    cv.add_text('Complete scholarship during the B.Sc. in Balseiro Institute.')
    cv.tab(-1)
    cv.step(2.5)

def add_posters_and_talks(cv):
    cv.add_text(CV().Text('Posters and talks', weight='bold'))
    cv.tab()
    cv.step()
    cv.add_text('Talk at the Q-Turn 2020 Workshop, Online. – '
                'November 23-27 2020.')
    cv.step(0.5)
    cv.add_text('Poster at the Annual Encounter of Nanoscience and '
                'Nanotechnology Institute,')
    cv.add_text('2020, Online. – July 21-23 2020.')
    cv.step(0.5)
    cv.add_text('Poster for the Advanced Laboratory subject\'s '
                'final examination – May 31, 2018.')
    cv.step(2.5)
    cv.tab(-1)

def add_attended_conferences(cv):
    cv.add_text(CV().Text('Attended conferences', weight='bold'))
    cv.tab()
    cv.step()
    cv.add_text('XXI Giambiagi Winter School 2019, Bs. As., Argentina. '
                'Quantum simulations and')
    cv.add_text('quantum metrology with cold trapped ions – July 15-24 2019.')
    cv.step(0.5)
    cv.add_text('Annual Meeting of Physics 2018, Bs. As., Argentina.')
    cv.step(2.5)
    cv.tab(-1)

cv = CV()
cv.set_endbar()
set_banner(cv)
cv.add_sectionbar("Education")
add_IB_MSc(cv)
cv.new_block()
cv.add_subsectionbar()
add_IB_BSc(cv)
cv.new_block()
cv.add_subsectionbar()
add_FCEIA_BSc(cv)
cv.new_block()
cv.add_sectionbar("Skills")
add_languages(cv)
cv.new_block()
cv.add_sectionbar("Experience")
add_posters_and_talks(cv)
cv.new_block()
cv.add_subsectionbar()
add_attended_conferences(cv)
cv.new_block()
cv.add_subsectionbar()
cv.add_text(CV().Text('My github: ')+
            CV().Text('https://github.com/NotBru.',
                      href='https://github.com/NotBru'))
cv.step(3)
cv.new_block()
cv.add_sectionbar("Honors")
add_scholarships(cv)
cv.write("CV English")
