<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * Get AsyncTask Response.
 */
class GetAsyncTaskResponse extends Model
{
    /**
     * @description async_task_id
     * type:string
     * @example 000e89fb-cf8f-11e9-8ab4-b6e980803a3b
     *
     * @var string
     */
    public $asyncTaskId;

    /**
     * @description message
     *
     * @example task is running
     *
     * @var string
     */
    public $message;

    /**
     * @description state
     *
     * @example success
     *
     * @var string
     */
    public $state;
    protected $_name = [
        'asyncTaskId' => 'async_task_id',
        'message'     => 'message',
        'state'       => 'state',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->asyncTaskId) {
            $res['async_task_id'] = $this->asyncTaskId;
        }
        if (null !== $this->message) {
            $res['message'] = $this->message;
        }
        if (null !== $this->state) {
            $res['state'] = $this->state;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetAsyncTaskResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['async_task_id'])) {
            $model->asyncTaskId = $map['async_task_id'];
        }
        if (isset($map['message'])) {
            $model->message = $map['message'];
        }
        if (isset($map['state'])) {
            $model->state = $map['state'];
        }

        return $model;
    }
}
