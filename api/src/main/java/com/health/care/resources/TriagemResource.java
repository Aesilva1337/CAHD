package com.health.care.resources;

import com.health.care.config.*;
import com.health.care.repository.TriagemRepository;
import com.health.care.repository.entity.Triagem;
import com.health.care.resources.dto.TriagemResponse;
import com.health.care.resources.dto.TriagemRequest;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;


@RestController
@RequestMapping(value=Config.PATH_BASE+"/triagem/",produces=MediaType.APPLICATION_JSON_UTF8_VALUE)
public class TriagemResource {

    @Autowired
    private TriagemRepository r;

    @Autowired
    private ModelMapper modelMapper;

    @PostMapping
    public TriagemResponse save(TriagemRequest req) {
        var model = modelMapper.map(req,Triagem.class);
        return modelMapper.map(r.save(model), TriagemResponse.class);
    }
}