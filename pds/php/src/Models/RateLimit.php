<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 下载限速配置.
 */
class RateLimit extends Model
{
    /**
     * @var int
     */
    public $partSize;

    /**
     * @var int
     */
    public $partSpeed;
    protected $_name = [
        'partSize'  => 'part_size',
        'partSpeed' => 'part_speed',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->partSize) {
            $res['part_size'] = $this->partSize;
        }
        if (null !== $this->partSpeed) {
            $res['part_speed'] = $this->partSpeed;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return RateLimit
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['part_size'])) {
            $model->partSize = $map['part_size'];
        }
        if (isset($map['part_speed'])) {
            $model->partSpeed = $map['part_speed'];
        }

        return $model;
    }
}
