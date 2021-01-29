<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class RemoveStoryImagesResultItem extends Model {
    protected $_name = [
        'code' => 'code',
        'fileId' => 'file_id',
        'isSucceed' => 'is_succeed',
        'message' => 'message',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->code) {
            $res['code'] = $this->code;
        }
        if (null !== $this->fileId) {
            $res['file_id'] = $this->fileId;
        }
        if (null !== $this->isSucceed) {
            $res['is_succeed'] = $this->isSucceed;
        }
        if (null !== $this->message) {
            $res['message'] = $this->message;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return RemoveStoryImagesResultItem
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['code'])){
            $model->code = $map['code'];
        }
        if(isset($map['file_id'])){
            $model->fileId = $map['file_id'];
        }
        if(isset($map['is_succeed'])){
            $model->isSucceed = $map['is_succeed'];
        }
        if(isset($map['message'])){
            $model->message = $map['message'];
        }
        return $model;
    }
    /**
     * @description code
     * @var string
     */
    public $code;

    /**
     * @description file_id
     * @var string
     */
    public $fileId;

    /**
     * @description is_succeed
     * @var bool
     */
    public $isSucceed;

    /**
     * @description message
     * @var string
     */
    public $message;

}
