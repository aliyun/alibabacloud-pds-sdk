<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 生成故事.
 */
class CreateStoryResponse extends Model
{
    /**
     * @var string
     */
    public $driveId;
    protected $_name = [
        'driveId' => 'drive_id',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return CreateStoryResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['drive_id'])) {
            $model->driveId = $map['drive_id'];
        }

        return $model;
    }
}
