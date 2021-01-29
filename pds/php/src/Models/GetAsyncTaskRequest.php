<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 获取异步人去信息
 */
class GetAsyncTaskRequest extends Model {
    protected $_name = [
        'asyncTaskId' => 'async_task_id',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->asyncTaskId) {
            $res['async_task_id'] = $this->asyncTaskId;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return GetAsyncTaskRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['headers'])){
            $model->headers = $map['headers'];
        }
        if(isset($map['async_task_id'])){
            $model->asyncTaskId = $map['async_task_id'];
        }
        return $model;
    }
    public $headers;

    /**
     * @description async_task_id
type:string
     * @example 000e89fb-cf8f-11e9-8ab4-b6e980803a3b
     * @var string
     */
    public $asyncTaskId;

}
