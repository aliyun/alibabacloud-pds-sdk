<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * list_file_by_anonymous base response
 */
class BaseFileAnonymousResponse extends Model {
    protected $_name = [
        'fileId' => 'file_id',
        'name' => 'name',
        'size' => 'size',
        'thumbnail' => 'thumbnail',
        'type' => 'type',
        'updatedAt' => 'updated_at',
    ];
    public function validate() {
        Model::validateMaxLength('fileId', $this->fileId, 50);
        Model::validateMinLength('fileId', $this->fileId, 40);
        Model::validatePattern('fileId', $this->fileId, '[a-z0-9]{1,50}');
        Model::validatePattern('name', $this->name, '[a-zA-Z0-9.-]{1,1000}');
        Model::validateMaximum('size', $this->size, 53687091200);
        Model::validateMinimum('size', $this->size, 0);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->fileId) {
            $res['file_id'] = $this->fileId;
        }
        if (null !== $this->name) {
            $res['name'] = $this->name;
        }
        if (null !== $this->size) {
            $res['size'] = $this->size;
        }
        if (null !== $this->thumbnail) {
            $res['thumbnail'] = $this->thumbnail;
        }
        if (null !== $this->type) {
            $res['type'] = $this->type;
        }
        if (null !== $this->updatedAt) {
            $res['updated_at'] = $this->updatedAt;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return BaseFileAnonymousResponse
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['file_id'])){
            $model->fileId = $map['file_id'];
        }
        if(isset($map['name'])){
            $model->name = $map['name'];
        }
        if(isset($map['size'])){
            $model->size = $map['size'];
        }
        if(isset($map['thumbnail'])){
            $model->thumbnail = $map['thumbnail'];
        }
        if(isset($map['type'])){
            $model->type = $map['type'];
        }
        if(isset($map['updated_at'])){
            $model->updatedAt = $map['updated_at'];
        }
        return $model;
    }
    /**
     * @description file_id
     * @example 5d5b846942cf94fa72324c14a4bda34e81da635d
     * @var string
     */
    public $fileId;

    /**
     * @description name
     * @example ccp.jpg
     * @var string
     */
    public $name;

    /**
     * @description size, type=file时才有效
     * @example 1024
     * @var int
     */
    public $size;

    /**
     * @description thumbnail
     * @example https://ccp.data.aliyuncs.com/hz22%2F5d5b986facbec311ef844c25954f96821497b383%2F5d5b986f955410dd991646bb87c6b4e899eff525?Expires=xxx&OSSAccessKeyId=xxx&Signature=xxx
     * @var string
     */
    public $thumbnail;

    /**
     * @description type
     * @example file
     * @var string
     */
    public $type;

    /**
     * @description updated_at
     * @var string
     */
    public $updatedAt;

}
