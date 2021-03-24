<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class GetRPVerifyResultRequest extends Model
{
    /**
     * @description During Verify Process, 是否在实人认证流程中调用
     *
     * @example true
     *
     * @var bool
     */
    public $duringVerifyProcess;

    /**
     * @description User ID, 当前访问的用户
     *
     * @example "2ef62459eb7a11ea932cacde48001122"
     *
     * @var string
     */
    public $userId;
    protected $_name = [
        'duringVerifyProcess' => 'during_verify_process',
        'userId'              => 'user_id',
    ];

    public function validate()
    {
        Model::validateRequired('userId', $this->userId, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->duringVerifyProcess) {
            $res['during_verify_process'] = $this->duringVerifyProcess;
        }
        if (null !== $this->userId) {
            $res['user_id'] = $this->userId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetRPVerifyResultRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['during_verify_process'])) {
            $model->duringVerifyProcess = $map['during_verify_process'];
        }
        if (isset($map['user_id'])) {
            $model->userId = $map['user_id'];
        }

        return $model;
    }
}
