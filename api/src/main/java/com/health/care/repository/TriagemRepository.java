package com.health.care.repository;

import com.health.care.repository.entity.Triagem;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface TriagemRepository extends MongoRepository<Triagem, String> {
    
}