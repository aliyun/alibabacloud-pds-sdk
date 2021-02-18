<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * Get AsyncTask Response
 */
class GetAsyncTaskResponse extends Model {
    protected $_name = [
        'asyncTaskId' => 'async_task_id',
        'consumedProcess' => 'consumed_process',
        'errCode' => 'err_code',
        'message' => 'message',
        'state' => 'state',
        'totalProcess' => 'total_process',
        'url' => 'url',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->asyncTaskId) {
            $res['async_task_id'] = $this->asyncTaskId;
        }
        if (null !== $this->consumedProcess) {
            $res['consumed_process'] = $this->consumedProcess;
        }
        if (null !== $this->errCode) {
            $res['err_code'] = $this->errCode;
        }
        if (null !== $this->message) {
            $res['message'] = $this->message;
        }
        if (null !== $this->state) {
            $res['state'] = $this->state;
        }
        if (null !== $this->totalProcess) {
            $res['total_process'] = $this->totalProcess;
        }
        if (null !== $this->url) {
            $res['url'] = $this->url;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return GetAsyncTaskResponse
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['async_task_id'])){
            $model->asyncTaskId = $map['async_task_id'];
        }
        if(isset($map['consumed_process'])){
            $model->consumedProcess = $map['consumed_process'];
        }
        if(isset($map['err_code'])){
            $model->errCode = $map['err_code'];
        }
        if(isset($map['message'])){
            $model->message = $map['message'];
        }
        if(isset($map['state'])){
            $model->state = $map['state'];
        }
        if(isset($map['total_process'])){
            $model->totalProcess = $map['total_process'];
        }
        if(isset($map['url'])){
            $model->url = $map['url'];
        }
        return $model;
    }
    /**
     * @description async_task_id
type:string
     * @example 000e89fb-cf8f-11e9-8ab4-b6e980803a3b
     * @var string
     */
    public $asyncTaskId;

    /**
     * @description consumed_process
     * @example 1024000
     * @var int
     */
    public $consumedProcess;

    /**
     * @description err_code
     * @example 200
     * @var int
     */
    public $errCode;

    /**
     * @description message
     * @example task is running
     * @var string
     */
    public $message;

    /**
     * @description state
     * @example success
     * @var string
     */
    public $state;

    /**
     * @description total_process
     * @example 4096000
     * @var int
     */
    public $totalProcess;

    /**
     * @description download_url
example
     * @var string
     */
    public $url;

}
