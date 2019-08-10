import { prop, Typegoose } from 'typegoose';
import { Student } from 'src/signup/models/student.model';
import { Interests } from 'src/signup/models/interests.model';

export class Parent extends Typegoose {
  @prop({ required: true, unique: true })
  student: Student;

  interests: Interests;

  @prop({ required: true })
  partnerShortcode: string;

  @prop()
  selfDescription: string;
}