#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 11:51:03 2021

@author: pengwei

copy from https://www.programcreek.com/python/?code=open-mmlab%2Fmmdetection%2Fmmdetection-master%2Fmmdet%2Fmodels%2Flosses%2Fmse_loss.py

"""


import torch
import torch.nn as nn
import torch.nn.functional as F


def mse_loss(pred, target):
    """Warpper of mse loss."""
    return F.mse_loss(pred, target, reduction='none')


class MSELoss(nn.Module):
    """MSELoss.

    Args:
        reduction (str, optional): The method that reduces the loss to a
            scalar. Options are "none", "mean" and "sum".
        loss_weight (float, optional): The weight of the loss. Defaults to 1.0
    """

    def __init__(self, reduction='mean', loss_weight=1.0):
        
        super().__init__()
        
        self.reduction = reduction
        self.loss_weight = loss_weight

    def forward(self, pred, target, weight=None, avg_factor=None):
        """Forward function of loss.

        Args:
            pred (torch.Tensor): The prediction.
            target (torch.Tensor): The learning target of the prediction.
            weight (torch.Tensor, optional): Weight of the loss for each
                prediction. Defaults to None.
            avg_factor (int, optional): Average factor that is used to average
                the loss. Defaults to None.

        Returns:
            torch.Tensor: The calculated loss
        """
        loss = self.loss_weight * mse_loss(
            pred,
            target,
            weight,
            reduction=self.reduction,
            avg_factor=avg_factor)
        return loss
    
