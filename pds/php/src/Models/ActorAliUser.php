<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class ActorAliUser extends Model
{
    /**
     * @description AliUserID
     *
     * @var string
     */
    public $aliUserId;

    /**
     * @description AliUserType
     *
     * @var string
     */
    public $aliUserType;
    protected $_name = [
        'aliUserId'   => 'ali_user_id',
        'aliUserType' => 'ali_user_type',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->aliUserId) {
            $res['ali_user_id'] = $this->aliUserId;
        }
        if (null !== $this->aliUserType) {
            $res['ali_user_type'] = $this->aliUserType;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return ActorAliUser
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['ali_user_id'])) {
            $model->aliUserId = $map['ali_user_id'];
        }
        if (isset($map['ali_user_type'])) {
            $model->aliUserType = $map['ali_user_type'];
        }

        return $model;
    }
}
