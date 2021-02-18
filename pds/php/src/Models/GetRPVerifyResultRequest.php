<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class GetRPVerifyResultRequest extends Model
{
    /**
     * @description User ID, 当前访问的用户
     *
     * @example "2ef62459eb7a11ea932cacde48001122"
     *
     * @var string
     */
    public $userId;
    protected $_name = [
        'userId' => 'user_id',
    ];

    public function validate()
    {
        Model::validateRequired('userId', $this->userId, true);
    }

    public function toMap()
    {
        $res = [];
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
        if (isset($map['user_id'])) {
            $model->userId = $map['user_id'];
        }

        return $model;
    }
}
