package com.health.care.domain;

import java.util.Date;

import lombok.Data;


@Data
public class Triagem{
    
    private Date dataInicial;

    private Triagem(){}

    public Triagem criarTriagem(){
        return new Triagem();
    }
}