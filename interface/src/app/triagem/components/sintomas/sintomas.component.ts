import { Component, OnInit } from '@angular/core';
import { TriagemService } from '../services/triagem.service';
import { SintomasModel } from '../models/components/sintomas.model';
import { FormBuilder, FormGroup, FormArray, FormControl, ValidatorFn } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';

@Component({
    selector: 'app-sintomas',
    templateUrl: './sintomas.component.html',
    styleUrls: ['./sintomas.component.scss']
  })
  export class SintomasComponent implements OnInit {
    constructor(
      private triagemService: TriagemService,
      private formBuilder: FormBuilder,
      private route: ActivatedRoute
    ) {
      this.route.params.subscribe(res => this.idDiagnostico = res.idDiagnostico);
    }

    public listSintomas: SintomasModel[] = [];
    public form: FormGroup;
    public idDiagnostico: number;

    async ngOnInit() {
      this.form = this.formBuilder.group({
        sintomas: new FormArray([])
      });

      const response = await this.triagemService.ListarSintomas({idDiagnostico: this.idDiagnostico});
      response.data.forEach(sintoma => this.listSintomas.push({
        id: sintoma.idSintoma,
        descricao: sintoma.descricaoSintoma,
        checked: false
      }));
    }

    checkboxSintoma(Sintoma: SintomasModel){
      Sintoma.checked = !Sintoma.checked;
      console.log(this.listSintomas)
    }
  }