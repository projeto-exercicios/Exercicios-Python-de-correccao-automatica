
# 2018/12/12 the initial content of theis script was copied from:
# ~/develop.old/articles/isel/leim/mdp/20172018a/trabalhos_de_casa/python_exercise_string_align_rigth_function/make_random_versions.py

# to import from text_transformer and py_transformer packages
import sys
#sys.path.append(
#    '/home/jbs/develop.old/articles/201509_python_exercises_generator')

#sys.path.append('/home/jbs/develop/201902_questions_transformer')
sys.path.append('../qom_questions_transformer')





import logging

# the logging file is defined by the script that uses this script
# logging.basicConfig(filename='util_make_random_versions.log',
#                     level=logging.DEBUG)

import os
import shutil

from random import choice
from random import randint
from random import seed

from pathlib import Path

# to load texts in the text manager
from text_transformer.tt_text_transformer_interface import load_text

# to load python sources in the python manager
from python_transformer.pt_util.pt_util_file import load_source_code_from_file
# # to construct program from parts
# from py_transformer.pt_nodes.pt_module import PTModule
from python_transformer.pt_source_code import PTSourceCode





def get_file_content(filename):

    with open(filename, "r") as f:
        content = f.read()

    return content





def write_to_file(filename, content):

    with open(filename, "w") as file:
        file.write(content)





def write_text_files(version_path, text_files_list, text_parts_list):

    for n in range(len(text_files_list)):

        text_file = text_files_list[n]
        text_part = text_parts_list[n]

        filename = os.path.join(version_path, text_files_list[n])
        content  = text_part.to_string()

        write_to_file(filename, content)





def write_seed(a_seed, version_path, seed_filename):

    filename = os.path.join(version_path, seed_filename)
    content  = str(a_seed)

    write_to_file(filename, content)





def read_seed(version_path, seed_filename):

    filename = os.path.join(version_path, seed_filename)
    print("aaa",filename)
    with open(filename, "r") as file:
        content = file.read()

    return int(content)





def write_output(out, err, excp, version_path, output_filename):

    filename = os.path.join(version_path, output_filename)
    content  = out +  err + excp

    write_to_file(filename, content)





def write_full_program(full_program, version_path, full_program_filename):

    filename = os.path.join(version_path, full_program_filename)
    content  = full_program

    write_to_file(filename, content)





def write_python_files(python_files_list, python_modules_list, version_path):

    for n in range(len(python_files_list)):
        filename = os.path.join(version_path, python_files_list[n])
        content  = python_modules_list[n].to_string()
        write_to_file(filename, content)





def link_fixed_files(fixed_files_list, version_path):

    for source in fixed_files_list:

        source_rel_path = os.path.relpath(source, version_path)
        destination     = os.path.join(version_path, source)

        logging.debug('link_fixed_files source_rel_path = ' + source_rel_path)
        logging.debug('link_fixed_files destination     = ' + destination)

        if os.path.exists(destination):

            logging.debug('link_fixed_files removing destination')
            os.remove(destination)

        os.symlink(source_rel_path, destination)
    




def copy_fixed_files(fixed_files_list, version_path):

    for source in fixed_files_list:

        destination = os.path.join(version_path, source)

        logging.debug('copy_fixed_files source      = ' + source)
        logging.debug('copy_fixed_files destination = ' + destination)

        if os.path.exists(destination):

            logging.debug('copy_fixed_files removing destination')
            os.remove(destination)

        shutil.copyfile(source, destination)
    




def make_random_versions(general_files_to_change_list,
                         python_files_list,
                         programs_to_run,
                         seed_filename,
                         make_transformations_script_filename,
                         number_of_versions,
                         version_path_prefix,
                         write_seed_flag,
                         true_or_false_alternative_answers,
                         fixed_files_list):

    # execution steps

    # added support for different python program saved in different
    # files 2017/11/17
    # added python stuff 2017/10/27
    # new 2017/09/25
    #

    # 0. import the function make_transformations from the
    #    make_transformations_script_filename file
    # 1. for each text file
    # 1a. read text file
    # 1b. load the text file in the text manager storing the returning part
    # 2. for each python file
    # 2a. read the python file
    # 2b. create the correspondent meta python object
    # 2c. for each configuration program
    # 2ci.   create the corresponding module
    # 2cii.  execute it
    # 2ciii. saved the program and output
    # 2civ.  confirm the answers output comparing it with the answers tex files
    # 3. for each version:
    # 3a. call the make_transformations function
    # 3b. write the managed texts to the version path
    # 3c. select true or false answers

    # 0
    cmd = "from " + make_transformations_script_filename \
         + " import make_transformations"
    print(cmd)
    exec("from " + make_transformations_script_filename
         + " import make_transformations")
    exec("from " + make_transformations_script_filename
         + " import make_transformations_on_results")

    from make_transformations import make_transformations
    from make_transformations import make_transformations_on_results

    # 1. read text files
    text_parts_list = []
    for filename in general_files_to_change_list:
        text      = get_file_content(filename)
        text_part = load_text(text)
        text_parts_list.append(text_part)
        
    # 2. read python files
    python_modules_list = []
    for filename in python_files_list:
        python_module = load_source_code_from_file(filename)
        python_modules_list.append(python_module)
        print("---------")
        print(python_module.to_string())
        #print("+++++++")
        #print(type(python_module))

    # 2c. for each configured program
    # 2ci.   create the corresponding module
    for n in range(len(programs_to_run)):
        program_to_run     = programs_to_run[n]
        program_files_list = program_to_run[0]
        full_program = PTSourceCode()
        for python_file in program_files_list:
            index = python_files_list.index(python_file)
            python_module = python_modules_list[index]
            full_program.append(python_module)
        print("+++++++")
        print(full_program.to_string())
        programs_to_run[n].append(full_program)

    # 2cii.  execute it
    # 2ciii. saved the program and output
    version_path = "" # to write in the current (main) directory
    for program_to_run in programs_to_run:
        full_program_file = program_to_run[1]
        output_file       = program_to_run[2]
        full_program      = program_to_run[3]

        write_full_program(full_program.to_string(), version_path,
                           full_program_file)
        (out, err, excp) = full_program.execute()
        write_output(out, err, excp, version_path, output_file)

    # just to change the current 20 in the first version
    randint(10, 20)

    # 3. for each version:
    for version in range(number_of_versions):

        version_path = version_path_prefix + str(version + 1)
        if not os.path.exists(version_path):
            os.makedirs(version_path)

        # 3a.
        if write_seed_flag == True:
            a_seed = randint(1000, 9999)
            write_seed(a_seed, version_path, seed_filename)
        else:
            a_seed = read_seed(version_path, seed_filename)

        seed(a_seed)

        make_transformations()

        for program_to_run in programs_to_run:
            full_program_file = program_to_run[1]
            output_file       = program_to_run[2]
            full_program      = program_to_run[3]
            write_full_program(full_program.to_string(), version_path,
                               full_program_file)
            (out, err, excp) = full_program.execute()
            print(out +  err + excp)
            write_output(out, err, excp, version_path, output_file)

        if len(programs_to_run) > 0:
            make_transformations_on_results(full_program)

        # 3b.
        # write the update texts to files
        write_text_files(version_path, general_files_to_change_list,
                         text_parts_list)

        write_python_files(python_files_list, python_modules_list, version_path)

        # to avoid versions dependencies fixed files should be copied
        # and no linked
        #link_fixed_files(fixed_files_list, version_path)
        copy_fixed_files(fixed_files_list, version_path)

        # 3c. select true or false answers
        # for answer in range(1, 6):

        #     if choice([True, False]) == True:
        #         command = "cp " + version_path + "/answer_" + str(answer) \
        #                   + "_true.tex " + version_path + "/answer_" \
        #                   + str(answer) + ".tex"

        #     else:
        #         command = "cp " + version_path + "/answer_" + str(answer) \
        #                   + "_false.tex " + version_path + "/answer_" \
        #                   + str(answer) + ".tex"

        #     print(command)
        #     os.system(command)
    
        #print('############')
        #print(os.getcwd())
        for (true_file, false_file, destination_file) \
            in true_or_false_alternative_answers:

            if choice([True, False]) == True:
                source_file = true_file
            else:
                source_file = false_file

            # source_path      = os.path.join(os.getcwd(), version_path,
            #                                 source_file)
            # destination_path = os.path.join(os.getcwd(), version_path,
            #                                 destination_file)

            source_path      = Path.cwd() / version_path / source_file
            destination_path = Path.cwd() / version_path / destination_file
            
            #curret_dir_fd    = os.open(os.getcwd(), os.O_RDONLY)
            #print('----------- ', curret_dir_fd)
            #print('----------- ', source_path)
            #print('----------- ', destination_path)
            
            if destination_path.exists():
                destination_path.unlink()

            # path_descriptor = os.open(version_path, os.O_RDONLY)

            # os.symlink(source_file,
            #            destination_file,
            #            dir_fd=path_descriptor)
            #            #dir_fd=curret_dir_fd)

            os.symlink(source_path, destination_path)
                       
