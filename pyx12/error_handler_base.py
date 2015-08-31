#pylint: disable-all
######################################################################
# Copyright Kalamazoo Community Mental Health Services,
#   John Holland <jholland@kazoocmh.org> <john@zoner.org>
# All rights reserved.
#
# This software is licensed as described in the file LICENSE.txt, which
# you should have received as part of this distribution.
#
######################################################################

"""
Base Interface to X12 Errors
"""

import abc
import logging
logger = logging.getLogger('pyx12.error_handler')


class ErrorHandlerBase(object):
    """
    Base class for the error handling structures.
    """
    __metaclass__  = abc.ABCMeta

    @abc.abstractmethod
    def accept(self, visitor):
        """
        Params:     visitor - ref to visitor class
        """

    @abc.abstractmethod
    def handle_errors(self, err_list):
        """
        @param err_list: list of errors to apply
        """

    @abc.abstractmethod
    def get_cur_line(self):
        """
        @return: Current file line number
        @rtype: int
        """

    @abc.abstractmethod
    def get_id(self):
        """
        """

    @abc.abstractmethod
    def add_isa_loop(self, seg_data, src):
        """
        @param seg_data: Segment object
        @type seg_data: L{segment<segment.Segment>}
        """

    @abc.abstractmethod
    def add_gs_loop(self, seg_data, src):
        """
        @param seg_data: Segment object
        @type seg_data: L{segment<segment.Segment>}
        """

    @abc.abstractmethod
    def add_st_loop(self, seg_data, src):
        """
        @param seg_data: Segment object
        @type seg_data: L{segment<segment.Segment>}
        """

    @abc.abstractmethod
    def add_seg(self, map_node, seg_data, seg_count, cur_line, ls_id):
        """
        @param map_node: current segment node
        @type map_node: L{node<map_if.segment_if>}
        @param seg_data: Segment object
        @type seg_data: L{segment<segment.Segment>}
        @param seg_count: Count of current segment in the ST Loop
        @type seg_count: int
        @param cur_line: Current line number in the file
        @type cur_line: int
        @param ls_id: The current LS loop identifier
        @type ls_id: string
        """

    @abc.abstractmethod
    def _add_cur_seg(self):
        """
        """

    @abc.abstractmethod
    def add_ele(self, map_node):
        """
        """

    @abc.abstractmethod
    def _add_cur_ele(self):
        """
        """

    @abc.abstractmethod
    def isa_error(self, err_cde, err_str):
        """
        @param err_cde: ISA level error code
        @type err_cde: string
        @param err_str: Description of the error
        @type err_str: string
        """

    @abc.abstractmethod
    def gs_error(self, err_cde, err_str):
        """
        @param err_cde: GS level error code
        @type err_cde: string
        @param err_str: Description of the error
        @type err_str: string
        """

    @abc.abstractmethod
    def st_error(self, err_cde, err_str):
        """
        @param err_cde: Segment level error code
        @type err_cde: string
        @param err_str: Description of the error
        @type err_str: string
        """

    @abc.abstractmethod
    def seg_error(self, err_cde, err_str, err_value=None, src_line=None):
        """
        @param err_cde: Segment level error code
        @type err_cde: string
        @param err_str: Description of the error
        @type err_str: string
        """

    @abc.abstractmethod
    def ele_error(self, err_cde, err_str, bad_value, refdes=None):
        """
        @param err_cde: Element level error code
        @type err_cde: string
        @param err_str: Description of the error
        @type err_str: string
        """

    @abc.abstractmethod
    def close_isa_loop(self, node, seg, src):
        pass

    @abc.abstractmethod
    def close_gs_loop(self, node, seg, src):
        pass

    @abc.abstractmethod
    def close_st_loop(self, node, seg, src):
        pass

    @abc.abstractmethod
    def find_node(self, type):
        """
        Find the last node of a type
        """

    @abc.abstractmethod
    def _get_last_child(self):
        pass


    @abc.abstractmethod
    def get_error_count(self):
        pass

    @abc.abstractmethod
    def get_first_child(self):
        pass

    @abc.abstractmethod
    def get_next_sibling(self):
        pass

    @abc.abstractmethod
    def __next__(self):
        """
        Return the next error node
        """

    @abc.abstractmethod
    def is_closed(self):
        """
        @rtype: boolean
        """

    @abc.abstractmethod
    def __repr__(self):
        """
        """

    @abc.abstractmethod
    def pop_errors(self):
        """
        Pop error list
        @return: List of errors
        """
